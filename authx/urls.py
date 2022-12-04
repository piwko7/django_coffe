from django.urls import re_path
from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import ActivationUserEmailView, LoginView, UserViewSet

router = DefaultRouter()

router.register(
    r"users",
    UserViewSet,
    basename="users",
)

urlpatterns = [
    re_path(r"", include(router.urls)),
    path("login", LoginView.as_view(), name="login"),
    path("activate/<slug:uidb64>/<slug:token>/", ActivationUserEmailView.as_view(), name="activate"),
]
