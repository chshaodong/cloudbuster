from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ansible_tasks.models import Task


class TaskListView(ListView):
    queryset = Task.objects.all()
    model = Task
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task


