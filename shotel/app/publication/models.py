from uuid import uuid4
from django.db import models
from django.conf import settings
from shotel.app.core.models import BaseModel
from .manager import PostQuerySet


class Post(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    content = models.TextField()
    image = models.ImageField(upload_to='posts/images/', null=True, blank=True)
    video = models.FileField(upload_to="posts/videos/", null=True, blank=True)
    post_likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='LikePost',
        related_name='like_posts'
    )

    objects = PostQuerySet.as_manager()


class Comment(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='LikeComment',
        related_name='liked_comments'
    )
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}"


class LikePost(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')


class LikeComment(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'comment')


class Notification(BaseModel):
    NOTIFICATION_TYPE = (
        ('LIKE', 'Like'),
        ('MSG', 'Message'),
        ('FOLLOW', 'Follow'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='receiver'
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sender'
    )
    notification_type = models.CharField(max_length=15, choices=NOTIFICATION_TYPE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True)
    is_seen = models.BooleanField(default=False)