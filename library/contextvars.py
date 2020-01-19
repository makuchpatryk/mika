from django.core.cache import cache

def context_data(request):
    music = cache.get('music', True)
    return {
        'MUSIC_PLAYING': music
    }
