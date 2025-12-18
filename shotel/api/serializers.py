from django.contrib.auth import get_user_model
from rest_framework import serializers
from shotel.app.entry.models import Profile
from shotel.app.user.models import Address

User = get_user_model()


class AddressMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['street', 'city', 'country']


class ProfilMiniSerializer(serializers.ModelSerializer):
    address = AddressMiniSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['avatar', 'address']


class UserMiniSerializer(serializers.ModelSerializer):
    profile = ProfilMiniSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

