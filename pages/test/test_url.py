from django.test import TestCase
from django.urls import reverse, resolve
from pages import views

class UrlTestCase(TestCase):
    def setUp(self):
        pass

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, views.IndexPageView)
