
from shotel.app.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'pk'},
            'password': {'write_only': True}
        }
        

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
        )
        return user
    

class LoginSerializer(serializers.Serializer):
    identifier = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ['identifier', 'password']
        extra_kwargs = {
            'passwrod': {'write_only': True}
        }
