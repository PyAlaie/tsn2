from django.urls import path

from .views import UserCreateAPIView

user_create = UserCreateAPIView.as_view()

urlpatterns = [
    path('create/', user_create, name='user_create'),
]
