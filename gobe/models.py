from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from django.db.models.signals import post_save 
from django.dispatch import receiver

#create your models here
class UserAccountManager(UserManager):
    
    def create_user(self, email, password):
        """User object constructor"""
        user = self.create(email=email, password=password)

        return user

class User(AbstractUser):
    """auth/login-related fields"""
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    # NOTE: before putting something here make sure it wouldn't be better in the profile model

    objects = UserAccountManager()


class Profile(models.Model):
    """non-auth-related/cosmetic fields"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=400)
    
    # Additional data that belongs to User profile
    # Examples:
    # Display Name
    # Bios, descriptions, taglines
    # Theme (light or dark)
    # email (if not used to log in)


#create a Profile and bind to a newly created User
"""receivers to add a Profile for newly created users"""
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
     if created:
         Profile.objects.create(user=instance)
@receiver(post_save, sender=User) 
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()
