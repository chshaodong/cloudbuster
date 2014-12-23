from django.shortcuts import render
from django.views.generic import ListView
from ansible_modules.models import AnsibleModule
import anyjson


class AnsibleModuleListView(ListView):
    queryset = AnsibleModule.objects.all()
    model = AnsibleModule
    context_object_name = "ansible_modules"
    
    def get(self, request, module_path=None):
        if module_path is not None:
            self.queryset = AnsibleModule.objects.filter(module_path__contains=module_path)
        return super(AnsibleModuleListView, self).get(request)

