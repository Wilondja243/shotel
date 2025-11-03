from django.urls import path, include
from rest_framework import routers

from shotel.api.user.views import UserApiView, LoginApiView
from shotel.api.user.views import UserViewSet


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)


urlpatterns = [
    path('account/signup/', UserApiView.as_view(), name="signup"),
    path('account/login/', LoginApiView.as_view(), name="login"),

    path('', include(router.urls))
]
