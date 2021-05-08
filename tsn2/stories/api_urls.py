from django.urls import path

from .api_views import StoryCreateAPIView, StoryDetailAPIView

story_create = StoryCreateAPIView.as_view()
story_detail = StoryDetailAPIView.as_view()


urlpatterns = [
    path('create/', story_create, name='story_create_api'),
    path('detail/<uuid:pk>/', story_detail, name='story_detail_api'),
]
