from django.conf.urls import patterns, include, url
from ansible_tasks.views import TaskListView, TaskDetailView

urlpatterns = patterns('',
        url(r'^tasks/$', TaskListView.as_view(), name='task_listview'),
        url(r'^tasks/(?P<pk>.+)/', TaskDetailView.as_view(), name='task_detailview'),
)

