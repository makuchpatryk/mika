from django.core.cache import cache
from django.conf import settings


def context_data(request):
    music = cache.get('music', True)
    return {
        'MUSIC_PLAYING': music,
        'P_AYPAL': settings.PAYPAL_CLIENT,
        'VERSION': settings.VERSION,
        'PR1C3': 30.00,
        # 'PR1C3': 00.10,
        'SITE_NAME': settings.SITE_NAME,
        'SITE_URL': settings.SITE_URL,
        'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID,
    }
