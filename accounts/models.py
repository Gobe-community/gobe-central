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
    bio = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    # NOTE: before putting something here make sure it wouldn't be better in the profile model
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def __str__(self):
        return self.get_full_name()

