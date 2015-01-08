from django.conf.urls import patterns, include, url
from ansible_modules.views import AnsibleModuleListView, show_categories

urlpatterns = patterns('',
    url(r'^modules/categories/$', show_categories),
    url(r'^modules/$', AnsibleModuleListView.as_view()),
    url(r'^modules/(?P<module_path>.+)/', AnsibleModuleListView.as_view()),
)
