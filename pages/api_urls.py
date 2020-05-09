from django.conf.urls import url, include
from . import api_views

urlpatterns = [
    url(r'^music-play/?$', api_views.MusicPlayView.as_view(), name="music_play"),
    url(r'^music-stop/?$', api_views.MusicStopView.as_view(), name="music_stop"),
    url(r'^like-post/?$', api_views.likePostView.as_view(), name="like_post"),
    url(r'^comment-post/?$', api_views.commentPostView.as_view(), name="comment_post"),
    url(r'^order-create/?$', api_views.OrderCreateView.as_view(), name="order_create"),
]
