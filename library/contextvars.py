from django.core.cache import cache

def context_data(request):
    music = cache.get('music')
    return {
        'MUSIC_PLAYING': music
    }
