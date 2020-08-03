from rest_framework import serializers

from .models import User, Profile


# #User serializer
# class UserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ['id','first_name', 'last_name', 'email', 'password']


#Profile serializer
class ProfileSerilalizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date', 'email_confirmed']


#SignUp form serializer
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerilalizer(required=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        #create profile
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.update_or_create(user=user, **profile_data)
        return user
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = profile_data.get('bio', profile.bio)
        profile.location = profile_data.get('location', profile.location)
        profile.birthdate = profile_data.get('birthdate', profile.birthdate)
        profile.email_confirmed = profile_data.get('email_confirmed', profile.email_confirmed)
        profile.save()

        return instance