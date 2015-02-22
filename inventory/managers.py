from django.db.models import Manager

class BaseVarManager(Manager):
    def bulk_update(self, vars):
        var_keys = [var['key'] for var in vars]
        for var in vars:
            obj, created = self.get_or_create(key=var['key'])
            obj.value = var['value']
            obj.save()
        vars_to_delete = self.exclude(key__in=var_keys)
        if vars_to_delete:
            for var in vars_to_delete:
                var.delete()

class InventoryVarManager(BaseVarManager):
        pass


