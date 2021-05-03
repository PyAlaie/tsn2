from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import User


class UserAdmin(auth_admin.UserAdmin):
    pass


admin.site.register(User, UserAdmin)
