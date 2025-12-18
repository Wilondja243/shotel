from uuid import uuid4
from django.db import models
from django.conf import settings

from shotel.app.core.models import BaseModel
from shotel.app.user.models import Address

class Profile(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    bio = models.TextField(blank=True)

    avatar = models.ImageField(
        upload_to="media/avatars/",
        blank=True, null=True
    )


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


