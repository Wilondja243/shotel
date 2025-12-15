from django.urls import path, include
from rest_framework import routers

from shotel.api.user.views import (
    UserViewSet,
    UserApiView,
    LoginApiView
)
from shotel.api.entry.views import (
    FollowerAPIView,
    FollowingAPIView,
    UnfollowAPIView,
    FollowAPIView,
)


router = routers.DefaultRouter()
router.register(r"users", UserViewSet, basename='user')


urlpatterns = [
    path('account/register/', UserApiView.as_view(), name="signup"),
    path('account/login/', LoginApiView.as_view(), name="login"),

    path('', include(router.urls)),
    path('followers/', FollowerAPIView.as_view(), name="follower"),
    path('following/', FollowingAPIView.as_view(), name="following"),
    path('follow/<uuid:user_id>/', FollowAPIView.as_view(), name="follow"),
    path('unfollow/<uuid:user_id>/', UnfollowAPIView.as_view(), name="unfollow"),
]
