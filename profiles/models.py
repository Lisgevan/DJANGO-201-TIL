from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField

#TODO: Delete image file when user is deleted

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
    
#signal - delete old avatar image file and not default one 
@receiver(models.signals.pre_save, sender=Profile)
def delete_file_on_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_image = Profile.objects.get(pk=instance.pk).image
        except Profile.DoesNotExist:
            return
        new_image = instance.image
        if old_image and old_image.url != new_image.url and old_image.url != '/media/default/default_avatar.png':
            old_image.delete(save=False)