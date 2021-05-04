from django.db import models
from django.contrib.auth import get_user_model
from location_field.models.plain import PlainLocationField
from mptt.models import MPTTModel, TreeForeignKey
from uuid import uuid4


class Post(MPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid4)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='meta')

    created_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Story(Post):
    location = PlainLocationField()
    title = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)


class Comment(Post):
    text = models.TextField(max_length=255)
