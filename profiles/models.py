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
    image = ImageField(upload_to='profiles', default= 'profiles/default_avatar.png')

    def __str__(self) -> str:
        return self.user.username

# signal function
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new Profile() object when a Django User is created."""
    if created:
        Profile.objects.create(user=instance)
    
@receiver(models.signals.pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Profile.objects.get(pk=instance.pk).image
    except Profile.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file and not old_file == 'profiles/default_avatar.png':
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)