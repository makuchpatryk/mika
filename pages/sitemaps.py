from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Snippet


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'o_mnie', 'feed', 'gallery', \
	    	'akustycznie', 'koncert', 'sesja_2016', 'sesja_2017', \
	    	'sesja_2019', 'sesja_2020', 'sesja_ayz', 'albums_almagest', \
	    	'albums_awe', 'albums_pyl', 'contact', 'elements', 'event']

    def location(self, item):
        return reverse(item)


class SnippetSitemap(Sitemap):
    def items(self):
        return Snippet.objects.all()

    def create(self, context):
        pass
