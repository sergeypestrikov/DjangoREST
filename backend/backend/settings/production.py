from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'backend',
        'USER': 'sergey',
        'PASSWORD': '12345',
        'HOST': 'db',
        'PORT': '5432',
    }
}