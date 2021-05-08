from rest_framework.serializers import ModelSerializer, CurrentUserDefault

from .models import Story


class StoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['location_x', 'location_y', 'title', 'description', 'created_by']
        extra_kwargs = {'created_by': {'default': CurrentUserDefault()}}
