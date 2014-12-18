from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ansible/', include('ansible_modules.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
