from rest_framework import serializers
from shotel.app.entry.models import Follower, Profil


class ProfilSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profil
        fields = ['user', 'profil', 'update_at', 'created_at']

class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follower
        fields = ['profil', 'user', 'update_at', 'created_at']

