from django.core.management.base import BaseCommand, CommandError
from ansible_modules import models
import os

class Command(BaseCommand):
    help = 'Builds and loads the module category tree into the database.'

    def handle(self, *args, **kwargs):
        
        modules = models.AnsibleModule.objects.all()
        module_paths = []
        for module in modules:
            module_paths.append(module.module_path)

        for module_path in module_paths:
            path = os.path.split(module_path)[0]
            module = models.AnsibleModule.objects.get(module_path=module_path)
            parents = []
            for part in path.split('/'):
                name = part
                if name == '':
                    name = None
                    parents.append(name)
                    continue
                
                if len(parents) > 0:  
                    parent = parents[-1]
                    if parent is None:
                        slug = "/%s" % part
                    else:
                        slug = "%s/%s" % (parent.slug, part)
                else:
                    parent = None
                    slug = "/%s" % part
                category, created = models.ModuleCategory.objects.get_or_create(name=name, 
                                                                            parent=parent,
                                                                            slug=slug)
                category.save()
                if slug != path:
                    parents.append(category)
                    continue
                else:
                    module.module_category = category
                    module.save()
