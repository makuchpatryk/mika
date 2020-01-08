from django.conf.urls import url, include
from . import api_views

urlpatterns = [
    url(r'^music-playing/?$', api_views.MusicPlayingView.as_view(), name="music_playing"),
]
