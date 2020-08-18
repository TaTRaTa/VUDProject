from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# There is two type of users: 1 for donor and 0 for needy. 
# For this purpose the new flag attribute donorOrNeedy has been added to User model. By default is needy.
class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donorOrNeedy = models.PositiveSmallIntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_type(sender, instance, created, **kwargs):
    if created:
        UserType.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_type(sender, instance, **kwargs):
    instance.UserType.save()