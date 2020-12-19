import requests
import json

from django.conf import settings


MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_AUDIENCE_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'


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
        return 'Done'