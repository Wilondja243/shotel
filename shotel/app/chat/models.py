from uuid import uuid4
from django.db import models
from django.conf import settings
from shotel.app.core.models import BaseModel


class Chat(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender_message")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver_message")
    message = models.CharField()

    class Meta:
        ordering = ['created_at',]