from rest_framework import serializers
from django.core.mail import send_mail

from .models import User


#User serializer
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'first_name', 'email', 'confirmed']