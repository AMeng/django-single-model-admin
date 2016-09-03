from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()
admin_url = url(r'^admin/', include(admin.site.urls))

try:
    from django.conf.urls import patterns
except ImportError:
    urlpatterns = [admin_url]
else:
    urlpatterns = patterns('', admin_url)
