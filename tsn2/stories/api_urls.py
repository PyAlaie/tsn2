from django.urls import path

from .api_views import StoryCreateAPIView

story_create = StoryCreateAPIView.as_view()


urlpatterns = [
    path('create/', story_create, name='story_create_api'),
]
