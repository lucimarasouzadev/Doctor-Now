from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'ixb6fha#ts=&b4t2u%p1_62-!8dw2j==j)d^3-j$!z(@*m+-h'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}