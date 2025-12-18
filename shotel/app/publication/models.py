from uuid import uuid4
from django.db import models
from django.conf import settings
from shotel.app.core.models import BaseModel


class Post(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Like', related_name='like_posts')


class Like(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')



class Notification(BaseModel):
    NOTIFICATION_TYPE = (
        ('LIKE', 'Like'),
        ('MSG', 'Message'),
        ('FOLLOW', 'Follow'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=15, choices=NOTIFICATION_TYPE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)
    is_seen = models.BooleanField(default=False)