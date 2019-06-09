# pages/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexPageView.as_view(), name='index'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^blog/$', views.AboutPageView.as_view(), name='blog'),
    url(r'^blog-single/$', views.AboutPageView.as_view(), name='blog_single'),
    url(r'^contact/$', views.AboutPageView.as_view(), name='contact'),
    url(r'^portfolio/$', views.AboutPageView.as_view(), name='portfolio'),
    url(r'^portfolio-single/$', views.AboutPageView.as_view(),name='portfolio_single'),
    url(r'^services/$', views.AboutPageView.as_view(), name='services')
]
