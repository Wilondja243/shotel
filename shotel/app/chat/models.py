from uuid import uuid4
from django.db import models
from django.conf import settings
from shotel.app.core.models import BaseModel


class Conversation(BaseModel):
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='conversations'
    )


class Message(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender_message")
    message = models.CharField()
    is_ready = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at',]
