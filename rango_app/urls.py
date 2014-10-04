from django.conf.urls import patterns, include, url
from django.contrib import admin
from rango_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),  
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),
)
