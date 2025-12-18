from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from shotel.app.user.models import Address


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profil(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def update_user_profil(sender, instance, **kwargs):
    try:
        instance.address.save()
    except Exception as e:
        print(f"Error {str(e)}")


@receiver(post_delete, sender=settings.AUTH_USER_MODEL)
def delete_user_profil(sender, instance, **kwargs):
    try:
        instance.address.delete()
    except Exception as e:
        print(f"Error {str(e)}")