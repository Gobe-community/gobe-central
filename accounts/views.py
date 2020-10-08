import requests
import json

from django.core.mail import send_mail
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

def subscribe(email):
        data = {
            "email_address": email,
            "status": "subscribed"
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
        sub_email = request.data['email']
        content = '''Welcome!
Kaabo 
Nabata
Barka da zuwa

Hello name of recipient
Thank you for joining our community and subscribing to our newsletter. Welcome on board. 
GoBe brings you relevant information, resourceful ideas, opinion, articles and educational publications 

For more details and enquiry insert a help line number or email
You can also find us on insert social media handles

We look forward to working together for creation of a  positive presence here.

Eshey 
Daalu 
Nagode
Thank you,
The GoBe Team'''
        # subscribe(email)
        send_mail('Welcome to goBE, {}'.format(request.data['first_name']),
                content,
                'everybees@gmail.com',
                [sub_email],
                fail_silently=False)
        return self.create(request, *args, **kwargs)
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