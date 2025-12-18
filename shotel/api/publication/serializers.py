from rest_framework import serializers
from rest_framework import serializers

from shotel.api.serializers import UserMiniSerializer
from shotel.app.publication.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = UserMiniSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'likes']


class CommentSerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content']

