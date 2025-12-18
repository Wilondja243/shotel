from rest_framework import serializers
from shotel.app.entry.models import Follower, Profile
from shotel.api.serializers import UserMiniSerializer


# Profil serializer
class ProfilSerializer(serializers.ModelSerializer):
    user = UserMiniSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'bio', 'update_at', 'created_at']


# Followers serializer
class FollowerSerializer(serializers.ModelSerializer):

    follower = UserMiniSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = [
            'id', 'follower', 'update_at', 'created_at'
        ]


# Following serializer
class FollowingSerializer(serializers.ModelSerializer):
    following = UserMiniSerializer(read_only=True)

    class Meta:
        model = Follower
        fields = [
            'id', 'following', 'update_at', 'created_at'
        ]