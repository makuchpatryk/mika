from django.shortcuts import render
# pages/views.py
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

