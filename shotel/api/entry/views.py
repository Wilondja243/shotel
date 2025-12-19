from django.shortcuts import get_object_or_404, redirect

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
    permission_classes = [IsAuthenticated,]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)

        if request.user == user_to_follow:
            return Response(
                {'message': "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        follower, created = Follower.objects.get_or_create(
            follower = request.user,
            following = user_to_follow
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


# class IsFollowAPIView(APIView):
#     permission_classes = [IsAuthenticated,]

#     def get(self, request, user_id):
#         user_to_follow = get_object_or_404(User, id=user_id)

#         is_following = Follower.objects.filter(
#             follower=request.user,
#             following=user_to_follow
#         ).exists()

#         return Response(
#             {"is_following": is_following},
#             status=status.HTTP_200_OK
#         )


class UnfollowAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    
    def delete(self, request, user_id):
        following = get_object_or_404(User, id=user_id)

        deleted, _ = Follower.objects.filter(
            follower = request.user,
            following = following
        ).delete()

        if not deleted:
            return Response(
                {'message': "You aren't following this user"}
            )

        return Response(
            {'message': "Unfollowed successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
