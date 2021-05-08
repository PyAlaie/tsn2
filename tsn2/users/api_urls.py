from django.urls import path

from .api_views import UserDeleteAPIView, UserRegisterAPIView, AuthLoginAPIView, AuthLogoutAPIView

user_register = UserRegisterAPIView.as_view()
user_delete = UserDeleteAPIView.as_view()
auth_login = AuthLoginAPIView.as_view()
auth_logout = AuthLogoutAPIView.as_view()

urlpatterns = [
    path('register/', user_register, name='user_register_api'),
    path('delete/', user_delete, name='user_delete_api'),
    path('login/', auth_login, name='auth_login_api'),
    path('logout/', auth_logout, name='auth_logout_api'),
]
