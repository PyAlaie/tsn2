from django.urls import path, include

urlpatterns = [
    #v1
    path('v1/users/', include('users.api.urls')),
]
