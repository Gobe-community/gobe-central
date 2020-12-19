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
