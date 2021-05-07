from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey

from uuid import uuid4
from random import randint

from .fields import XField, YField


class Post(MPTTModel):
    id = models.UUIDField(primary_key=True, default=uuid4)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='meta')

    created_by = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


HIDESPOT_RATE = settings.STORIES['HIDESPOT_RATE']


class Story(Post):
    location_x = XField()
    location_y = YField()

    hidespot_x = XField(default=0, editable=False)
    hidespot_y = YField(default=0, editable=False)

    title = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    def _gen_hidespot(self, x, y):
        rand1 = randint(-50, 50) / HIDESPOT_RATE
        rand2 = randint(-50, 50) / HIDESPOT_RATE

        hsx = max(-90, min(90, x + rand1))
        hsy = max(-180, min(180, y + rand2))

        return hsx, hsy

    def save(self, *args, **kwargs):
        self.hidespot_x, self.hidespot_y = self._gen_hidespot(self.location_x, self.location_y)
        super(Story, self).save(*args, **kwargs)


class Comment(Post):
    text = models.TextField(max_length=255)
