from uuid import uuid4
from django.db import models
from django.conf import settings

from shotel.app.core.models import BaseModel


class Profil(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profil = models.ImageField(upload_to="media", blank=True, null=True)


class Follower(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="follower"
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following"
    )

    class Meta:
        unique_together = ("follower", "following")


class Notification(BaseModel):
    NOTIFICATION_TYPE = (
        ('follower', 'Follower'),
        ('update', 'Update'),
        ('user', 'user'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)

