from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mbf_localdb',
        'USER': 'mbf_user',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    }
}
