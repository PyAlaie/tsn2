from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .serializers import StorySerializer, StoryHidenSerializer
from .models import Story


class StoryCreateAPIView(CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class StoryHidenAPIView(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryHidenSerializer


class StoryDetailAPIView(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]


class StoryDeleteAPIView(DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
