from django.urls import path, include
from shotel.app.user.views import SignupView, LoginView
from shotel.app.chat.views import HomeView, ChatView

urlpatterns = [
    # user
    path("signup/", SignupView.as_view(), name="signup"),
    path("account/login/", LoginView.as_view(), name="login"),

    # chat
    path("home/", HomeView.as_view(), name="home"),
    path("chat/<uuid:receive_id>/", ChatView.as_view(), name="chat")
]
