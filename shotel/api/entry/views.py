from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView
)

from shotel.app.user.models import User
from shotel.app.entry.models import Follower
from shotel.api.entry.serializers import (
    ProfilSerializer,
    FollowerSerializer,
    FollowingSerializer
)


class FollowerAPIView(ListAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Follower.objects.filter(
            follower=self.request.user).distinct()
    

class FollowingAPIView(ListAPIView):
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Follower.objects.filter(
            following=self.request.user).distinct()
    

class FollowAPIView(APIView):

    def post(self, request, user_id):
        if request.user.id == user_id:
            return Response(
                {'message': "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        follower, created = Follower.objects.get_or_create(
            follower = request.user,
            following = user_id
        )

        if not created:
            return Response(
                {'message': "Already Following"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response(
            {'message': "Followed successufully"},
            status=status.HTTP_201_CREATED
        )


class UnfollowAPIView(APIView):
    
    def delete(self, request, user_id):
        deleted, _ = Follower.objects.filter(
            follower = request.user,
            following = user_id
        ).delete()

        if not deleted:
            return Response(
                {'message': "You aren't following this user"}
            )

        return Response(
            {'message': "Unfollowed successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
