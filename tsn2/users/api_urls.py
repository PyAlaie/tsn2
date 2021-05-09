from django.urls import path

from .api_views import (
    UserDetailAPIView,
    UserGetAPIView,
    UserDeleteAPIView,
    UserRegisterAPIView,
    AuthLoginAPIView,
    AuthLogoutAPIView
)

user_detail = UserDetailAPIView.as_view()
user_get = UserGetAPIView.as_view()
user_register = UserRegisterAPIView.as_view()
user_delete = UserDeleteAPIView.as_view()
auth_login = AuthLoginAPIView.as_view()
auth_logout = AuthLogoutAPIView.as_view()

urlpatterns = [
    path('<str:email>', user_detail, name='user_detail_api'),
    path('get_user/<str:slug>/', user_get, name='user_get_api'),
    path('register/', user_register, name='user_register_api'),
    path('delete/', user_delete, name='user_delete_api'),
    path('login/', auth_login, name='auth_login_api'),
    path('logout/', auth_logout, name='auth_logout_api'),
]
