from django.conf.urls import patterns, include, url
from ansible_modules.views import AnsibleModulesList

urlpatterns = patterns('',
    url(r'^modules/$', AnsibleModulesList.as_view()),
)
