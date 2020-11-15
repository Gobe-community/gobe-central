from .base import *

DEBUG = False
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', env('DOMAIN_NAME')]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# django_heroku.settings(locals())

DATABASES = {
    'default': dj_database_url.config(
        default= env.db('DATABASE_URL'),
        conn_max_age=600
    )
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SENDGRID_API_KEY = env('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

MAILCHIMP_API_KEY = env('MAILCHIMP_API_KEY')
MAILCHIMP_DATA_CENTER = env('MAILCHIMP_DATA_CENTER')
MAILCHIMP_AUDIENCE_ID = env('MAILCHIMP_AUDIENCE_ID')
