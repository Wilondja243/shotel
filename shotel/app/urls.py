from django.urls import path, include
from shotel.app.user.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home")
]
