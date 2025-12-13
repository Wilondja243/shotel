from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView
)

from shotel.app.user.models import User
from shotel.api.entry.serializers import ProfilSerializer, FollowerSerializer


class FollowerAPIView(ListAPIView):
    serializer_class = FollowerSerializer

    def get_queryset(self):
        return User.objects.filter(
            is_my_follower=True, id=self.request.user.id).exclude(id=self.request.user.id)
    
    def get(self, request):
        followers = self.get_queryset()
        serializer = FollowerSerializer(followers, many=True, context={'request': request})
        
        return Response(
            {
                'success_message': 'Followers get successfully',
                'objects': { "followers": serializer.data }
            },
            status=status.HTTP_201_CREATED
        )