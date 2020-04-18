from django.core.cache import cache
from django.conf import settings

def context_data(request):
    music = cache.get('music', True)
    return {
        'MUSIC_PLAYING': music,
        'P_AYPAL': settings.PAYPAL_CLIENT,
        'VERSION': settings.VERSION,
        # 'PR1C3': 34.10,
        'PR1C3': 00.10,
    }
