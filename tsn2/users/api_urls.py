from django.urls import path

from .api_views import UserRegisterAPIView, UserDestroyAPIView, AuthLoginAPIView, AuthLogoutAPIView

user_register = UserRegisterAPIView.as_view()
user_destroy = UserDestroyAPIView.as_view()
auth_login = AuthLoginAPIView.as_view()
auth_logout = AuthLogoutAPIView.as_view()

urlpatterns = [
    path('register/', user_register, name='user_register_api'),
    path('destroy/<slug:pk>/', user_destroy, name='user_destroy_api'),
    path('login/', auth_login, name='auth_login_api'),
    path('logout/', auth_logout, name='auth_logout_api'),
]
