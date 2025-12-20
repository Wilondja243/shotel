import numpy as np
from django.db import models
from django.apps import apps
from django.forms import FloatField
from django.utils import timezone
from django.db.models import Window
from django.db.models.functions import (
    Now, Power,
    PercentRank,
)
from django.db.models import (
    Subquery,
    OuterRef,
    Count, F,
    ExpressionWrapper
)


class PostQuerySet(models.QuerySet):
    def post_rank(self, user, top_percentile=90):
        Address = apps.get_model('user', 'Address')

        user_country = Address.objects.filter(user=user).values('country')[:1]

        hours_since_post=ExpressionWrapper(
            Now() - F("created_at"),
            output_field=FloatField()
        )

        likes_count = Count('post_likes')

        popularity = ExpressionWrapper(
            likes_count / Power(hours_since_post + 1, 0.5),
            output_field=FloatField()
        )

        qs = self.annotate(
            hours_since_post=hours_since_post,
            likes_count=likes_count,
            popularity=popularity,
        )

        regional_posts = qs.filter(author__address__country=Subquery(user_country))
        global_posts = qs.exclude(author__address__country=Subquery(user_country))

        global_posts = global_posts.annotate(
            rank=Window(
                expression=PercentRank(),
                order_by=F('popularity').desc()
            )
        ).filter(rank__gte=(top_percentile / 100.0))

        return regional_posts.union(global_posts).order_by('-popularity')


class PostManager(models.Manager):
    def show_post(self, user):
        pass