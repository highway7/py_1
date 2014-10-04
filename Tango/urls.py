from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^rango_app/', include('rango_app.urls')),
    url(r'^ssn_demo/', include('ssn_demo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)



# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )