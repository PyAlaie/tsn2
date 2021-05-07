from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserCreateAPIView

user_create = UserCreateAPIView.as_view()

urlpatterns = [
    path('create/', user_create, name='user_create'),
    path('login/', obtain_auth_token, name='login'),
]
