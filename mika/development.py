import os
from .base import *
from .safe import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATIC_ROOT = '/storage/home/django_learn/storage/static/'
EMAIL_RECIVER_USER = 'makuchpatryk@gmail.com'

SECURE_SSL_REDIRECT = False