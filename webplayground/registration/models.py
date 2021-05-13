from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


def custom_uploads_to(instance, filename):
    """
    @param instance
    An instance of the model where the FileField is defined. More specifically, this is the particular instance where
    the current file is being attached.

    In most cases, this object will not have been saved to the database yet, so if it uses the default AutoField, it
    might not yet have a value for its primary key field.

    @param filename
    The filename that was originally given to the file. This may or may not be taken into account when determining the
    final destination path.
    """
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_uploads_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
