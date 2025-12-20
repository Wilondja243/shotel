from django.urls import path, include
from rest_framework import routers

from shotel.api.user.views import (
    UserViewSet,
    UserApiView,
    LoginApiView,
    UserMeAPIView,
    ProfileDetailView,
    AddressUpdateView
)
from shotel.api.entry.views import (
    FollowerAPIView,
    FollowingAPIView,
    UnfollowAPIView,
    FollowAPIView,
)
from shotel.api.publication.views import (
    PostCreateView,
    PostListView,
    CommentCreateView,
    CommentListView,
    ToggleLikeAPIView,
    ToggleLikeCommentAPIView,
)
from shotel.api.chat.views import (
    ConversationListView
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename='user')


urlpatterns = [
    path('account/register/', UserApiView.as_view(), name="signup"),
    path('account/login/', LoginApiView.as_view(), name="login"),

    # User
    path('', include(router.urls)),
    path('user/me/', UserMeAPIView.as_view(), name="me"),
    path('user/profile/', ProfileDetailView.as_view(), name="profile"),
    path('user/address/', AddressUpdateView.as_view(), name="address"),

    # Follower
    path('followers/', FollowerAPIView.as_view(), name="follower"),
    path('following/', FollowingAPIView.as_view(), name="following"),
    path('follow/<uuid:user_id>/', FollowAPIView.as_view(), name="follow"),
    # path('follow/is-following/<uuid:user_id>/', IsFollowAPIView.as_view(), name="is_following"),
    path('follwing/unfollow/<uuid:user_id>/', UnfollowAPIView.as_view(), name="unfollow"),

    # Conversation
    path('conversation/', ConversationListView.as_view(), name="conversation"),

    # Publication
    path('post/rank/', PostListView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name="post-create"),
    path('post/comment-create/<uuid:post_id>/', CommentCreateView.as_view(), name="comment"),
    path('post/comment-list/<uuid:post_id>/', CommentListView.as_view(), name="comment-list"),
    path('post/post-like/<uuid:post_id>/', ToggleLikeAPIView.as_view(), name='post-like'),
    path('post/comment-like/<uuid:comment_id>/', ToggleLikeCommentAPIView.as_view(), name='comment-like'),
]
