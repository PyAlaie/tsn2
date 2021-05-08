from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .serializers import StoryCreateSerializer, StorySerializer
from .models import Story


class StoryCreateAPIView(CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class StoryDetailAPIView(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
