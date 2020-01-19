from django.core.cache import cache
from django.conf import settings

def context_data(request):
    music = cache.get('music', True)
    return {
        'MUSIC_PLAYING': music,
        'VERSION': settings.VERSION
    }
