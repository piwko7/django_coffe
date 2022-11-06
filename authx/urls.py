from django.urls import re_path
from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import LoginView, UserViewSet

router = DefaultRouter()

router.register(
    r"users",
    UserViewSet,
    basename="users",
)

urlpatterns = [
    re_path(r"", include(router.urls)),
    path("login", LoginView.as_view(), name="login"),
]
