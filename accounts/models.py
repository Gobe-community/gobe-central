from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from .managers import UserAccountManager


#create your models here
class User(AbstractUser):
    """auth/login-related fields"""
    username = None
    email = models.EmailField(unique=True)
    confirmed = models.BooleanField(default=False)
    
    # NOTE: before putting something here make sure it wouldn't be better in the profile model
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserAccountManager()

    def __str__(self):
        return self.email
