# pages/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^blog/$', views.BlogPageView.as_view(), name='blog'),
    url(r'^gallery/$', views.GalleryPageView.as_view(), name='gallery'),
    url(r'^albums-store/$', views.AlbumsStorePageView.as_view(), name='albums_store'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^elements/$', views.ElementsPageView.as_view(), name='elements'),
    url(r'^event/$', views.EventPageView.as_view(),name='event'),
]
