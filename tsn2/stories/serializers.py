from rest_framework.serializers import ModelSerializer, CurrentUserDefault, ValidationError

from .models import Story


class StorySerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'location_x', 'location_y', 'title', 'description', 'created_at', 'created_by']
        extra_kwargs = {'created_by': {'default': CurrentUserDefault}}
        read_only_fields = ['id', 'created_at']

    def validate_created_by(self, value):
        if value != self.context['request'].user:
            raise ValidationError('User is not current user')
        return value




class StoryHidenSerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'hidespot_x', 'hidespot_y', 'title', 'description', 'created_at', 'created_by']
