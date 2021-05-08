from django.urls import path, include

app_name = 'api'

urlpatterns = [
    #v1
    path('v1/', include([
        path('users/', include('users.api_urls')),
        path('stories/', include('stories.api_urls')),
    ]))
]
