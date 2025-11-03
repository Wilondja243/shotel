from django.urls import path, include
from rest_framework import routers

from shotel.api.user.views import UserApiView, LoginApiView


urlpatterns = [
    path('account/signup/', UserApiView.as_view(), name="signup"),
    path('account/login/', LoginApiView.as_view(), name="login"),
]
