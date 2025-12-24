import base64
from rest_framework import serializers
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField, Base64FileField

from shotel.api.serializers import UserMiniSerializer
from shotel.app.publication.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = UserMiniSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    image = Base64ImageField(require=False)
    video = Base64FileField(required=False)

    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'video', 'likes_count']
        extra_kwargs = {'author': {'read_only': True}}


    def get_likes_count(self, obj):
        return obj.post_likes.count()
    
    def validate(self, data):
        if not data.get('content') and not data.get('image') and not data.get('video'):
            raise serializers.ValidationError("Post can't be empty.")
        return data


class CommentSerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content']
        extra_kwargs = {
            'user': {'read_only': True},
            'post': {'read_only': True}
        }

