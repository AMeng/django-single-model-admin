from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

try:
    from django.conf.urls import patterns
except ImportError:
    urlpatterns = [url(r'^admin/', admin.site.urls)]
else:
    urlpatterns = patterns('', url(r'^admin/', include(admin.site.urls)))
