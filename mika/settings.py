import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT = '/home/patryk/project/storage/static/'

PAYPAL_TEST = False


PAYPAL_CLIENT = 'PAYPAL_SANDBOX_CLIENT'
PAYPAL_SECRET = 'PAYPAL_SANDBOX_SECRET'

SECURE_SSL_REDIRECT = True