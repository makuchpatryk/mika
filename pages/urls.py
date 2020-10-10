# pages/urls.py
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index'),
    url(r'<slug:slug>/', views.snippet_detail),
    url(r'^o-mnie/$', views.AboutPageView.as_view(), name='o_mnie'),
    url(r'^tablica/?$', views.feed, name='feed'),
    url(r'^post/(?P<slug>[\w\-\_]+)/?$', views.post, name='post'),

    url(r'^galeria/$', views.GalleryView.as_view(), name='gallery'),
    url(r'^galeria/akustycznie/$', views.akustycznie, name='akustycznie'),
    url(r'^galeria/koncert/$', views.koncert, name='koncert'),
    url(r'^galeria/sesja-1/$', views.Sesja_2016, name='sesja_2016'),
    url(r'^galeria/sesja-2/$', views.Sesja_2017, name='sesja_2017'),
    url(r'^galeria/sesja-3/$', views.Sesja_2019, name='sesja_2019'),
    url(r'^galeria/sesja-4/$', views.Sesja_2020, name='sesja_2020'),
    url(r'^galeria/sesja-ayz/$', views.sesja_ayz, name='sesja_ayz'),
    url(r'^galeria/sesja-turkus/$', views.sesja_turkus, name='sesja_turkus'),

    url(r'^album-almagest/$', views.AlbumsAlmagestPageView.as_view(), name='albums_almagest'),
    url(r'^album-awe/$', views.AlbumsAwePageView.as_view(), name='albums_awe'),
    url(r'^album-pyl/$', views.AlbumsPylPageView.as_view(), name='albums_pyl'),
    url(r'^kontakt/$', views.ContactPageView.as_view(), name='contact'),

    url(r'^order-form/?$', views.OrderFormView.as_view(), name='order_form'),
    url(r'^order-payment/?$', views.order_payment, name='order_payment'),

    url(r'^order-success/?$', views.order_success, name='order_success'),
    url(r'^order-fail/?$', views.order_fail, name='order_fail'),
    url(r'^order-cancel/?$', views.order_cancel, name='order_cancel'),

    url(r'^sent-confimation/(?P<pk>\d+)/?$', views.sent_confimation, name='sent_confimation'),
]
