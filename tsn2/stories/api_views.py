from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from .serializers import StorySerializer, StoryHidenSerializer, CommentSerializer
from .models import Story, Comment


class StoryCreateAPIView(generics.CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class StoryHidenAPIView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryHidenSerializer


class StoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated]


class StoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class CommentAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset
        obj = get_object_or_404(queryset, parent=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
