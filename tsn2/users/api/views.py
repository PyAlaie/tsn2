from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserSerializer


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer


class UserLoginAPIView(ObtainAuthToken):
    pass


class UserLogoutAPIView(APIView):
    def post(self, request, format=None):
        request.user.auth_token.delete()
        response = {
            "datails": "logged out."
        }
        return Response(response, status=HTTP_200_OK)

