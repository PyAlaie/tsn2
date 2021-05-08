from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import StoryCreateSerializer


class StoryCreateAPIView(CreateAPIView):
    serializer_class = StoryCreateSerializer
    permission_classes = [IsAuthenticated]
