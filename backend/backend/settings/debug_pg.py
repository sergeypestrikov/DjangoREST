from .debug import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'backend',
        'USER': 'sergey',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '54328',
    }
}