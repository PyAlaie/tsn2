from django.urls import path, include

app_name = 'api'

urlpatterns = [
    # v1
    path('v1/', include([
        path('users/', include('users.api_urls', namespace='users')),
        path('stories/', include('stories.api_urls', namespace='stories')),
    ]))
]
