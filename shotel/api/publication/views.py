from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    CreateAPIView,
    RetrieveAPIView
)
from shotel.api.publication.serializers import (
    PostSerializer,
    CommentSerializer,
)
from shotel.app.publication.models import (
    LikeComment,
    Post,
    Comment,
    LikePost
)


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return Post.objects.post_rank(self.request.user)


class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        response.data = {
            "message": "Commentaire publié avec success!",
            "status": status.HTTP_202_ACCEPTED
        }

        return response

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(user=self.request.user, post=post)


class CommentListView(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]
    
    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return Comment.objects.filter(post=post).select_related('user')
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        response.data = {
            "count": len(response.data),
            "objects": response.data,
        }
        
        return response


class ToggleLikeAPIView(APIView):
    def post(self, request, post_id):
        user = request.user

        post = get_object_or_404(Post, id=post_id)

        like_exits = LikePost.objects.filter(user=user, post=post)

        if like_exits.exists():
            like_exits.delete()
            return Response(
                {"message": "Unliked", "is_liked": False}
            )
        else:
            LikePost.objects.create(user=user, post=post)

            return Response(
                {"message": "Liked", "is_liked": True},
                status=status.HTTP_201_CREATED
            )


class ToggleLikeCommentAPIView(APIView):
    def post(self, request, comment_id):
        user = request.user

        comment = get_object_or_404(Comment, id=comment_id)

        like_exits = LikeComment.objects.filter(user=user, comment=comment)

        if like_exits.first():
            like_exits.delete()
            return Response(
                {"message": "Unliked", "is_liked": False}
            )
        else:
            LikeComment.objects.create(user=user, comment=comment)

            return Response(
                {"message": "Liked", "is_liked": True},
                status=status.HTTP_201_CREATED
            )
