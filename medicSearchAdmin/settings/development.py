import os.path

from .settings import *

DEBUG = True

SECRET_KEY = 'ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6dˆ3-j$!z(@*m+-h'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}