from rest_framework import serializers
from shotel.app.entry.models import Follower, Profil
from shotel.api.serializers import UserMiniSerializer


# Profil serializer
class ProfilSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profil
        fields = ['user', 'profil', 'update_at', 'created_at']


# Followers serializer
class FollowerSerializer(serializers.ModelSerializer):
    follower = UserMiniSerializer(read_only = True)

    class Meta:
        model = Follower
        fields = ['id', 'follower', 'update_at', 'created_at']


# Following serializer
class FollowingSerializer(serializers.ModelSerializer):
    follower = UserMiniSerializer(read_only = True)

    class Meta:
        model = Follower
        fields = ['id', 'following', 'update_at', 'created_at']