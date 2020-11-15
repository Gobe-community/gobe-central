from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from .managers import UserAccountManager
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

from django.db.models.signals import post_save 
from django.dispatch import receiver

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


# class Newsletter(models.Model):

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     subject = models.CharField(max_length=150)
#     contents = models.FileField(upload_to='uploaded_newsletters/')

#     def __str__(self):
#         return self.subject + " " + self.created_at.strftime("%B %d, %Y")

#     def send(self, request):
#         content = self.contents.read().decode('utf-8')
#         users = User.objects.filter(confirmed=True)
#         for sub in users:
#             subject = self.subject
#             html_content = content + ('<br><a href="{}?email={}">Unsubscribe</a>.').format(
#                             request.build_absolute_uri('/frontend/api/delete/'), sub.email)
#             html_content_stripped = strip_tags(html_content)
#             from_email = 'everybees@gmail.com'
#             to_email = sub.email

#             send_mail(subject, html_content_stripped, from_email, [to_email], fail_silently=False)