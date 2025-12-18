from django.urls import path, include
from rest_framework import routers

from shotel.api.user.views import (
    UserViewSet,
    UserApiView,
    LoginApiView,
    UserMeAPIView
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
    ToggleLikeAPIView,
    ToggleLikeCommentAPIView,
)

# from shotel.api.chat.views import (
#     SendMessageAPIView,
# )

router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename='user')


urlpatterns = [
    path('account/register/', UserApiView.as_view(), name="signup"),
    path('account/login/', LoginApiView.as_view(), name="login"),
    path('user/me/', UserMeAPIView.as_view(), name="me"),

    # User
    path('', include(router.urls)),

    # Follower
    path('followers/', FollowerAPIView.as_view(), name="follower"),
    path('following/', FollowingAPIView.as_view(), name="following"),
    path('follow/<uuid:user_id>/', FollowAPIView.as_view(), name="follow"),
    # path('follow/is-following/<uuid:user_id>/', IsFollowAPIView.as_view(), name="is_following"),
    path('follwing/unfollow/<uuid:user_id>/', UnfollowAPIView.as_view(), name="unfollow"),

    # Conversation
    # path('conversation/send-message/', SendMessageAPIView.as_view(), name="send-message")

    # Publication
    path('post/', PostListView.as_view(), name='post'),
    path('post/create/', PostCreateView.as_view(), name="post-create"),
    path('post/post-like/<uuid:post_id>/', ToggleLikeAPIView.as_view(), name='post-like'),
    path('post/comment-like/<uuid:comment_id>/', ToggleLikeCommentAPIView.as_view(), name='comment-like'),

]
