from django.conf.urls import patterns, include, url

from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name="home"),
    #url(r'^\?(P<fb_id>)|(tu_id)$', views.home, name="home"),
    url(r'^polls/', include('apps.polls.urls', namespace="polls")),
    url(r'^accounts/', include('django_facebook.auth_urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^facebook/', include('django_facebook.urls'))
)
