from django.db import models

class ModuleCategoryManager(models.Manager):
    
    def root_categories(self, **kwargs):
        return self.filter(parent__isnull=True, **kwargs)
