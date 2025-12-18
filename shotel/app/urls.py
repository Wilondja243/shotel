from django.urls import path, include
from shotel.app.user.views import SignupView, LoginView
from shotel.app.chat.views import ChatView
from shotel.app.entry.views import (
    HomeView,
    FriendView,
    FollowerView
)
from shotel.app.publication.stream import notification_stream

urlpatterns = [
    # user
    path("signup/", SignupView.as_view(), name="signup"),
    path("account/login/", LoginView.as_view(), name="login"),

    # entry
    path("", HomeView.as_view(), name="home"),
    path("home/friends/", FriendView.as_view(), name="friend"),
    path("home/follower", FollowerView.as_view(), name="follower"),
    path("chat/<uuid:receive_id>/", ChatView.as_view(), name="chat"),

    # Notification stream
    path("home/stream/notification/", notification_stream, name="notification_stream")
]
