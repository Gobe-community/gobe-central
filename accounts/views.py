import requests
import json

from rest_framework.views import APIView
from rest_framework import generics
from django.conf import settings

from .models import User
from .serializers import UserSerializer

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_AUDIENCE_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'

# Create your views here.

# subscribe user to mailchimp with first_name and email
def subscribe(email, first_name):
        data = {
            "email_address": email,
            "status": "subscribed",
            'merge_fields': {
                'FNAME': first_name
            }
        }
        r = requests.post(
            members_endpoint,
            auth=("", MAILCHIMP_API_KEY),
            data=json.dumps(data)
        )
        return r.status_code, r.json()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs): 
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        sub_email = request.data.get('email')
        subscribe_to_newsletter = request.data.get('confirmed', False)
        first_name = request.data.get('first_name')

        # Register user if they click the subscribe checkbox
        # if (subscribe_to_newsletter != False):
        subscribe(sub_email, first_name)
        # print("Subscribed")

        return self.create(request, *args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
                return self.destroy(request, *args, **kwargs)