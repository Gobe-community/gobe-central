from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.response import Response

import accounts.models as acm
import accounts.serializers as acs
import accounts.tasks as act


# Create your views here.


class SubscribeUserToNewsLetter(viewsets.ModelViewSet):
    queryset = acm.User.objects.all()
    serializer_class = acs.UserSerializer

    def create(self, request):
        serializer = acs.UserSerializer(data=request.data)

        try:
            email = request.data.get('email')
            first_name = request.data.get('first_name')

            if serializer.is_valid():
                serializer.save()

                # subscibes user to mailchimp
                act.subscribe(email, first_name)
            
            elif IntegrityError:
                return Response({"message": "User with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "User created and subscribed."})
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)