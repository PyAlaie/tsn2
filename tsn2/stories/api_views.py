from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .serializers import StoryCreateSerializer, StoryViewSerializer, StoryDetailSerializer
from .models import Story


class StoryCreateAPIView(CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class StoryAPIView(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryViewSerializer


class StoryDetailAPIView(RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer
    permission_classes = [IsAuthenticated]


class StoryDeleteAPIView(DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryDetailSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
