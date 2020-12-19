from rest_framework import viewsets
from rest_framework.response import Response

import accounts.models as acm
import accounts.serializers as acs
import accounts.tasks as act


class SubscribeUserToNewsLetterViewSet(viewsets.ModelViewSet):
    queryset = acm.User.objects.all()
    serializer_class = acs.UserSerializer

    def create(self, request):
        serializer = acs.UserSerializer(data=request.data)

        try:
            email = request.data.get('email')
            first_name = request.data.get('first_name')
            confirmed = request.data.get('confrimed', False)

            if serializer.is_valid():
                serializer.save()

            # subscribes user to mailchimp
            act.subscribe(email, first_name)

            return Response({"message": "User created and subscribed."})
        except Exception as e:
            return Response({"message": str(e)})