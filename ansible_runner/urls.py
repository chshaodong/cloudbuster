from django.conf.urls import patterns, include, url
from ansible_runner.views import adhoc_runner

urlpatterns = patterns('',
        url(r'^adhoc/$', adhoc_runner), 
)

