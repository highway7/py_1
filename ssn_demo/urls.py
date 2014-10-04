from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from ssn_demo import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^vpns/', views.listvpn, name='vpns'),
    url(r'^add_vpn/', views.addvpn, name='add_vpn'),
)
