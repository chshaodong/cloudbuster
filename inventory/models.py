from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from ansible import utils

class Inventory(models.Model):
    name = models.CharField(_('name'), max_length=40)
    vars = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def get_hosts(self):
        return self.hosts.all()

    def get_groups(self):
        return self.host_groups.all()

    def add_group(self, name):
        return HostGroup.objects.create(inventory=self, name=name)

    def set_variable(self, key, value):
        kv = {key: value}
        if self.vars is None:
            self.vars = kv 
        else:
            self.vars = utils.combine_vars(self.vars, kv)
        return self.save()

    def get_variables(self):
        return self.vars



class HostGroup(MPTTModel):
    inventory = models.ForeignKey('Inventory', related_name='host_groups')
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True)
    name = models.CharField(_(u'name'), max_length=40)
    vars = models.TextField(blank=True, null=True)
    depth = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['parent__name', 'name',]
        unique_together = ('name', 'parent', 'inventory')
        verbose_name = _('host_group',)
        verbose_name_plural = _('host_groups',)
    
    def add_child_group(self, group):
        return self.children.add(group)

    def add_host(self, host):
        return self.hosts.add(host)

    def set_variable(self, key, value):
        kv = {key: value}
        if self.vars is None:
            self.vars = kv 
        else:
            self.vars = utils.combine_vars(self.vars, kv)
        return self.save()

    def get_hosts(self):
        return self.hosts.all()

    def get_variables(self):
        return self.vars

    def get_ancestors(self):
        """not implemented"""
        pass


class Host(models.Model):
    inventory = models.ForeignKey('Inventory', related_name='hosts')
    groups = models.ManyToManyField('HostGroup', related_name='hosts', blank=True, null=True)
    name = models.TextField()
    vars = models.TextField(blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def add_group(self, group):
        return self.groups.add(group)

    def set_variable(self, key, value):
        kv = {key: value}
        if self.vars is None:
            self.vars = kv 
        else:
            self.vars = utils.combine_vars(self.vars, kv)
        return self.save()

    def get_groups(self):
        return self.groups.all()
    
    def get_variables(self):
        return self.vars



