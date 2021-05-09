from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import User, UserSlug


@receiver(post_save, sender=User)
def slug_handler(sender, instance, created, **kwargs):
    if created:
        slug_name = slugify(instance.fullname)
        slug_instance = UserSlug(user=instance, slug_name=slug_name)
        slug_instance.save()


@receiver(post_save, sender=UserSlug)
def slug_id_handler(sender, instance, **kwargs):
    if instance.slug_id == 0:
        queryset = sender.objects.filter(slug_name=instance.slug_name)
        instance.slug_id = len(queryset)
        instance.save()
