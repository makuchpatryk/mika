# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nc8r5!q_i3f@91&#+7!94u8fy!d#3&^avh)6@=_)awbdgfjb9j'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mika',
        'USER': 'mika',
        'PASSWORD': 'tomasz',
        'HOST': 'localhost',
        'PORT': '',
    }
}

FACEBOOK_APP_ID = 285761572453773

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tomasz.s.mika@gmail.com'
EMAIL_HOST_PASSWORD = 'Makuch1.'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_RECIVER_USER = 'teespeem@gmail.com'