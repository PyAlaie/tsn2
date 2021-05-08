from django.urls import path, include

from .api_views import StoryCreateAPIView, StoryAPIView, StoryDetailAPIView, StoryDeleteAPIView

story_create = StoryCreateAPIView.as_view()
story_view = StoryAPIView.as_view()
story_detail = StoryDetailAPIView.as_view()
story_delete = StoryDeleteAPIView.as_view()


urlpatterns = [
    path('create/', story_create, name='story_create_api'),
    path('<uuid:pk>/', include([
        path('', story_view, name='story_view_api'),
        path('detail/', story_detail, name='story_detail_api'),
        path('delete/', story_delete, name='story_delete_api'),
    ])
    ),
]
