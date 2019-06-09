from django.shortcuts import render
# pages/views.py
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class PortfolioPageView(TemplateView):
    template_name = 'portfolio.html'


class PortfolioSinglePageView(TemplateView):
    template_name = 'portfolio-single.html'


class ServicesPageView(TemplateView):
    template_name = 'services.html'


class BlogPageView(TemplateView):
    template_name = 'blog.html'


class BlogSinglePageView(TemplateView):
    template_name = 'blog-single.html'
