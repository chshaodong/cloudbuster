from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloudbuster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^ansible/', include('ansible_modules.urls')),
    url(r'^ansible/', include('inventory.urls')),
    url(r'^ansible/', include('ansible_tasks.urls')),
    url(r'^api/', include('inventory.api.urls')),
    url(r'^api/', include('ansible_modules.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
