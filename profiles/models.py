from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField
import os

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,  
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = ImageField(upload_to='profiles', default= 'default/default_avatar.png')

    def __str__(self) -> str:
        return self.user.username

# signal function
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new Profile() object when a Django User is created."""
    if created:
        Profile.objects.create(user=instance)
    
# @receiver(models.signals.pre_save, sender=Profile)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` object is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False

#     try:
#         old_file = Profile.objects.get(pk=instance.pk).image
#     except Profile.DoesNotExist:
#         return False

#     new_file = instance.image
#     if old_file and old_file.url not in (new_file.url, 'default/default_avatar.png'):
#         old_file.delete(save=False)
#     else: 
#         if not old_file == new_file:
#             if os.path.isfile(old_file.path):
#                 os.remove(old_file.path)

@receiver(models.signals.pre_save, sender=Profile)
def delete_file_on_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_image = Profile.objects.get(pk=instance.pk).image
            print('old image test')
            print(old_image)
            print(type(old_image))
            print(old_image.url)
            print('old image test end')
        except Profile.DoesNotExist:
            return
        new_image = instance.image
        if old_image and old_image.url != new_image.url and old_image.url != '/media/default/default_avatar.png':
            old_image.delete(save=False)