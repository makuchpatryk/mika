from django.shortcuts import render
# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from .forms import NameForm, PreorderForm
from django.contrib import messages
from django.core.cache import cache

import os
from django.conf import settings

from django.templatetags.static import static


class IndexPageView(FormView):
    template_name = 'index.html'
    form_class = PreorderForm
    success_url = '/'

    def form_valid(self, form):
        emial = form.send_email()
        if emial:
            return render(self.request, 'index.html', {
                'form': form, 'message_sent': True})
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = NameForm
    success_url = '/'

    def form_valid(self, form):
        emial = form.send_email()
        if emial:
            return render(self.request, 'contact.html', {
                'form': form, 'message_sent': True})
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AlbumsAlmagestPageView(TemplateView):
    template_name = 'albums/almagest.html'

class AlbumsAwePageView(TemplateView):
    template_name = 'albums/awe.html'

class AlbumsPylPageView(FormView):
    template_name = 'albums/pyl.html'
    form_class = PreorderForm
    success_url = '/'

    def form_valid(self, form):
        emial = form.send_email()

        if emial:
            return render(self.request, 'albums/pyl.html', {
                'form': form, 'message_sent': True})
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class ElementsPageView(TemplateView):
    template_name = 'elements.html'


class EventPageView(TemplateView):
    template_name = 'event.html'


class BlogPageView(TemplateView):
    template_name = 'blog.html'


class GalleryView(TemplateView):
    template_name = 'gallery-main.html'


def akustycznie(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/akustycznie/')
    context = {'images' : img_list, 'folder': 'akustycznie'}
    return render(request, "gallery/gallery.html", context)


def koncert(request):
    path = settings.STATICFILES_DIRS[0]

    img_list = os.listdir(path + '/img/gallery/koncert/')
    context = {'images' : img_list, 'folder': 'koncert'}
    return render(request, "gallery/gallery.html", context)

def Sesja_2016(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/sesja_2016/')
    context = {'images' : img_list, 'folder': 'sesja_2016'}
    return render(request, "gallery/gallery.html", context)


def Sesja_2017(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/sesja_2017/')
    context = {'images' : img_list, 'folder': 'sesja_2017'}
    return render(request, "gallery/gallery.html", context)


def Sesja_2019(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/sesja_2019/')
    context = {'images' : img_list, 'folder': 'sesja_2019'}
    return render(request, "gallery/gallery.html", context)


def sesja_ayz(request):
    path = settings.STATICFILES_DIRS[0]
    img_list = os.listdir(path + '/img/gallery/sesja_ayz/')
    context = {'images' : img_list, 'folder': 'sesja_ayz'}
    return render(request, "gallery/gallery.html", context)
