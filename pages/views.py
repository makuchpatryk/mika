from django.shortcuts import render
# pages/views.py
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class AlbumsStorePageView(TemplateView):
    template_name = 'albums-store.html'


class ElementsPageView(TemplateView):
    template_name = 'elements.html'


class EventPageView(TemplateView):
    template_name = 'event.html'


class BlogPageView(TemplateView):
    template_name = 'blog.html'

