from django.shortcuts import render
from django.views.generic import ListView

from ansible_modules.models import AnsibleModule

class AnsibleModulesList(ListView):
    query_set = AnsibleModule.objects.all()
    model = AnsibleModule
    context_object_name = "ansible_modules"
