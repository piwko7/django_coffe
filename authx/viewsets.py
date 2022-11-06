from datetime import datetime, timedelta

from django.contrib.auth import get_user_model, logout
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.utils.translation import gettext_lazy as _
from authx.jwt import create_jwt
from authx.permissions import IsOwnerUser

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()  # .order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsOwnerUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        logout(request)
        self.perform_destroy(instance)

        return Response(status=HTTP_204_NO_CONTENT)


class LoginView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed(_("User not found"))

        if not user.check_password(password):
            raise AuthenticationFailed(_("Incorrect password"))

        payload = {
            "id": user.id,
            "exp": datetime.utcnow() + timedelta(minutes=60),
            "iat": datetime.utcnow(),
        }

        token = create_jwt(payload)

        return Response({"jwt": token})
