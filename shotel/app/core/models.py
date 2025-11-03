from django.db import models
from django.utils import timezone


class BaseQueryset(models.QuerySet):

    def delete(self, **kwargs):
        return super().update(delete_at = timezone.now())
    

class BaseModelManager(models.Manager):

    def get_queryset(self):
        return BaseQueryset(self.model, using=self._db).filter(delete_at=None)
    

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(blank=True, null=True)

    objects = BaseModelManager()

    class Meta:
        abstract = True

    def delete(self):
        self.delete_at = timezone.now()
        self.save()

