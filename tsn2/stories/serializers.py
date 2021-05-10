from rest_framework import serializers

from .models import Story, Comment


class StorySerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='comment_list_api'
    )

    class Meta:
        model = Story
        fields = ['id', 'location_x', 'location_y', 'title', 'description', 'created_at', 'created_by', 'comments']
        extra_kwargs = {'created_by': {'default': serializers.CurrentUserDefault}}
        read_only_fields = ['id', 'created_at']

    def validate_created_by(self, value):
        if value != self.context['request'].user:
            raise serializers.ValidationError('User is not current user')
        return value


class StoryHidenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'hidespot_x', 'hidespot_y', 'title', 'description', 'created_at', 'created_by']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_by','text']
        read_only_fields = ['id', 'created_by']
