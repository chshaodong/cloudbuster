from django.conf.urls import patterns, include, url
from ansible_modules.views import AnsibleModuleListView

urlpatterns = patterns('',
    url(r'^modules/$', AnsibleModuleListView.as_view()),
)
