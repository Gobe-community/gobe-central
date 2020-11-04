import requests
import json

from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.template.loader import render_to_string, get_template
from django.template import Context
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

# subscribe user with mailchimp
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
        subscribe_to_newsletter = request.POST.get('confirmed', False)
        first_name = request.data['first_name']

        # Register user if they click the subscribe checkbox
        if (subscribe_to_newsletter != False):
            subscribe(sub_email)

        # Sending Weolcome Mail to user
        plaintext = get_template('welcome_mail.txt')
        htmly = get_template('welcome_mail.html')
        context = { "first_name": first_name }
        subject, from_email, to = 'Welcome to GO-BE', 'everybees@gmail.com', sub_email
        text_content = plaintext.render(context)
        html_content = htmly.render(context)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

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