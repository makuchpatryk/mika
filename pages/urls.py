# pages/urls.py
from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^blog/$', views.BlogPageView.as_view(), name='blog'),

    url(r'^gallery/$', views.GalleryView.as_view(), name='gallery'),
    url(r'^gallery/akustycznie/$', views.akustycznie, name='akustycznie'),
    url(r'^gallery/koncert/$', views.koncert, name='koncert'),
    url(r'^gallery/sesja-1/$', views.Sesja_2016, name='sesja_2016'),
    url(r'^gallery/sesja-2/$', views.Sesja_2017, name='sesja_2017'),
    url(r'^gallery/sesja-3/$', views.Sesja_2019, name='sesja_2019'),
    url(r'^gallery/sesja-ayz/$', views.sesja_ayz, name='sesja_ayz'),

    url(r'^albums-almagest/$', views.AlbumsAlmagestPageView.as_view(), name='albums_almagest'),
    url(r'^albums-awe/$', views.AlbumsAwePageView.as_view(), name='albums_awe'),
    url(r'^albums-pyl/$', views.AlbumsPylPageView.as_view(), name='albums_pyl'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^elements/$', views.ElementsPageView.as_view(), name='elements'),
    url(r'^event/$', views.EventPageView.as_view(),name='event'),
]
