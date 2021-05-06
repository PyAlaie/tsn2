from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
