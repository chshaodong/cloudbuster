from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from ansible_modules.models import AnsibleModule, ModuleCategory
import anyjson


class AnsibleModuleListView(ListView):
    queryset = AnsibleModule.objects.all()
    model = AnsibleModule
    context_object_name = "ansible_modules"
    
    def get(self, request, module_path=None):
        if module_path is not None:
            self.queryset = AnsibleModule.objects.filter(module_path__contains=module_path)
        return super(AnsibleModuleListView, self).get(request)
    def get_context_data(self, **kwargs):
        context = super(AnsibleModuleListView, self).get_context_data(**kwargs)
        context['nodes'] = ModuleCategory.objects.all()
        return context

def show_categories(request):
    return render_to_response("ansible_modules/categories.html", 
                                {'nodes': ModuleCategory.objects.all()},
                                context_instance=RequestContext(request))

                    
