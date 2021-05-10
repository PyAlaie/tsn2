from django.urls import path, include

urlpatterns = [
    # v1
    path('v1/', include([
        path('users/', include('users.api_urls'), name='users'),
        path('stories/', include('stories.api_urls'), name='stories'),
    ]))
]
