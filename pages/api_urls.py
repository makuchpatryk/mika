from django.conf.urls import url, include
from . import api_views

urlpatterns = [
    url(r'^music-play/?$', api_views.MusicPlayView.as_view(), name="music_play"),
    url(r'^music-stop/?$', api_views.MusicStopView.as_view(), name="music_stop"),
]
