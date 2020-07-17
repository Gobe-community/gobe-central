from rest_framework import serializers

from .models import User


#User serializer
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'password']


#SignUp form serializer
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(
                validated_data['first_name'],
                validated_data['last_name'],
                validated_data['email'],
                validated_data['password']
            )
            return user