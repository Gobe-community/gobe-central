from rest_framework import serializers

import accounts.models as acm


#User serializer
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = acm.User
        fields = ['id', 'first_name', 'email', 'confirmed']
        read_only_fields = ['id']
