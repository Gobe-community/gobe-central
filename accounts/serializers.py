from rest_framework import serializers

from .models import User


#User serializer
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email']

        extra_kwargs = {
            'password': {'write_only': True},
        }


#Profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    #user = UserSerializer(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'bio', 'location', 'birth_date']


#SignUp form serializer
class SignupSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            
            #create user
            user = User.objects.create_user(
                validated_data['first_name'],
                validated_data['last_name'],
                validated_data['email'],
                validated_data['password']
            )

            profile_data = validated_data.pop('profile')
            #create profile
            profile = Profile.objects.create(
                user = user,
                bio = profile_data['bio'],
                location = profile_data['location'],
                birthdate= profile_data['birth_date'],
                email_confirmed = ['email_confirmed']
            )
            return user