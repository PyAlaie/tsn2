from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.text import slugify

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=60)
    date_joined = models.DateField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    slug_name = models.SlugField(max_length=120)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'password']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.fullname)
        super(User, self).save(*args, **kwargs)
