import random

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.text import slugify

from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=60)
    date_joined = models.DateField(auto_now_add=True, editable=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    slug_name = models.SlugField(max_length=120)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.fullname)
        super(User, self).save(*args, **kwargs)
