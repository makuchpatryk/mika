
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from pages import api_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('pages.urls')),
    url(r'^api/', include('pages.api_urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
