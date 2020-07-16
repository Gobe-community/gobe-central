from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from .managers import UserAccountManager

from django.db.models.signals import post_save 
from django.dispatch import receiver

#create your models here
class User(AbstractUser):
    """auth/login-related fields"""
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    # NOTE: before putting something here make sure it wouldn't be better in the profile model
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def __str__(self):
        return self.get_full_name()


class Profile(models.Model):
    """non-auth-related/cosmetic fields"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    
    # Additional data that belongs to User profile
    # Examples:
    # Date_of_birth
    # Bios, descriptions, taglines


#create a Profile and bind to a newly created User
"""receivers to add a Profile for newly created users"""
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(user=instance)
     instance.profile.save()
