from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, TokenSerializer


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer


class UserLoginAPIView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    parser_classes = api_settings.DEFAULT_PARSER_CLASSES
    throttle_classes = api_settings.DEFAULT_THROTTLE_CLASSES
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES

    serializer_class = TokenSerializer


class UserLogoutAPIView(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        response = {
            "datails": "logged out."
        }
        return Response(response, status=HTTP_200_OK)
