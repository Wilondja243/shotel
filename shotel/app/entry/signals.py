from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from .models import Profil


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profil(sender, instance, created, **kwargs):

    if created:
        Profil.objects.create(user=instance)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def update_user_profil(sender, instance, **kwargs):
#     try:
#         instance.empployerprofil.save()
#     except Exception as e:
#         print(f"Error {str(e)}")


# @receiver(post_delete, sender=settings.AUTH_USER_MODEL)
# def delete_user_profil(sender, instance, **kwargs):
#     try:
#         if instance.role == "candidate":
#             instance.candidateprofil.delete()
#         elif instance.role == "employer":
#             instance.empployerprofil.delete()
#         else:
#             print(f"Something went wrong to update profil")
#     except Exception as e:
#         print(f"Error {str(e)}")