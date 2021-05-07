from django.urls import path

from .api_views import UserRegisterAPIView, UserLoginAPIView, UserLogoutAPIView

user_register = UserRegisterAPIView.as_view()
user_login = UserLoginAPIView.as_view()
user_logout = UserLogoutAPIView.as_view()

urlpatterns = [
    path('register/', user_register, name='user_register_api'),
    path('login/', user_login, name='user_login_api'),
    path('logout/', user_logout, name='user_logout_api'),
]
