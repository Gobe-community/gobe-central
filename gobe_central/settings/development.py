from .base import *

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

MAILCHIMP_API_KEY = env('MAILCHIMP_API_KEY')
MAILCHIMP_DATA_CENTER = env('MAILCHIMP_DATA_CENTER')
MAILCHIMP_AUDIENCE_ID = env('MAILCHIMP_AUDIENCE_ID')