
from shotel.app.user.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    following_ids = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'following_ids']
        extra_kwargs = {
            'url': {'view_name': 'user-detail', 'lookup_field': 'pk'},
            'password': {'write_only': True}
        }

    
    def get_following_ids(self, obj):
        return list(obj.following.values_list('following_id', flat=True))

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
