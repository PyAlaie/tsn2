from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, DjangoObjectPermissions
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from .serializers import UserSerializer, TokenSerializer
from .models import User


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    lookup_url_kwarg = ''

    def get_object(self):
        return self.request.user


class AuthLoginAPIView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    parser_classes = api_settings.DEFAULT_PARSER_CLASSES
    throttle_classes = api_settings.DEFAULT_THROTTLE_CLASSES
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    serializer_class = TokenSerializer


class AuthLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)
