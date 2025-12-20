from django.db import models
from django.apps import apps
from django.db.models import FloatField
from django.utils import timezone
from django.db.models import Window, Func
from django.db.models.functions import (
    Now, Power,
    PercentRank,
    Cast
)
from django.db.models import (
    Subquery,
    OuterRef,
    Count, F,
    Value,
    ExpressionWrapper
)


class PostQuerySet(models.QuerySet):
    def post_rank(self, user, top_percentile=90):
        Address = apps.get_model('user', 'Address')

        user_country = Address.objects.filter(user=user).values('country')[:1]

        qs = self.annotate(
            hours_since_post=ExpressionWrapper(
                Func(Now() - F("created_at"), function='EXTRACT', 
                    template="EXTRACT(EPOCH FROM %(expressions)s)") / 3600.0 + 1.0,
                output_field=FloatField()
            )
        ).annotate(
            popularity=ExpressionWrapper(
                (Count('post_likes') * 1.0) / Power(F('hours_since_post'), 0.5),
                output_field=FloatField()
            )
        )

        regional_posts = qs.filter(author__address__country=Subquery(user_country))
        global_pool = qs.exclude(
            author__address__country=Subquery(user_country)
        ).annotate(
            percent_rank=Window(
                expression=PercentRank(),
                order_by=F('popularity').desc()
            )
        )

        global_ids = [
            p.id for p in global_pool 
            if p.percent_rank is not None and p.percent_rank >= (top_percentile / 100.0)
        ]

        global_posts = qs.filter(id__in=global_ids)

        return (global_posts | regional_posts).distinct().order_by('-popularity')
