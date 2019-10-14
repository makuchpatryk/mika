from django.shortcuts import render
# pages/views.py
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from .forms import NameForm
from django.contrib import messages

import os
from django.conf import settings

from django.templatetags.static import static


class IndexPageView(TemplateView):
    template_name = 'index.html'


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


class AlbumsStorePageView(TemplateView):
    template_name = 'albums-store.html'


class ElementsPageView(TemplateView):
    template_name = 'elements.html'


class EventPageView(TemplateView):
    template_name = 'event.html'


class BlogPageView(TemplateView):
    template_name = 'blog.html'


def gallery_almagest(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images/aYz-Domoslawice/')
    context = {'images' : img_list, 'folder': 'aYz-Domoslawice'}
    return render(request, "gallery/gallery.html", context)


def ayz_proba(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path + '/images/aYz-proba/')
    context = {'images' : img_list, 'folder': 'aYz-proba'}
    return render(request, "gallery/gallery.html", context)
