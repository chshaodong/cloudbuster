from django.contrib import admin
from ansible_tasks.models import Task

admin.site.register(Task)
