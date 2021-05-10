from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Story, Comment


class StorySerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedIdentityField(
        view_name='api:stories:comment_list_api'
    )

    created_by = serializers.SerializerMethodField('get_slug')

    def get_slug(self, obj):
        view_name = 'api:users:user_get_api'
        url_kwargs = {"slug": obj.created_by.userslug.slug}
        request = self.context['request']

        return reverse(viewname=view_name, kwargs=url_kwargs, request=request)

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
    created_by = serializers.SerializerMethodField('get_slug')

    def get_slug(self, obj):
        view_name = 'api:users:user_get_api'
        url_kwargs = {"slug": obj.created_by.userslug.slug}
        request = self.context['request']

        return reverse(viewname=view_name, kwargs=url_kwargs, request=request)

    class Meta:
        model = Comment
        fields = ['id', 'created_by', 'text']
        read_only_fields = ['id', 'created_by']
