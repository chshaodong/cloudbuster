from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from ansible import utils

class BaseVar(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField(null=True, blank=True)
    class Meta:
        abstract = True

class Inventory(models.Model):
    name = models.CharField(_('name'), max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
   
    def __unicode__(self):
        return "%s" % self.name

    def get_hosts(self):
        return self.hosts.all()

    def get_groups(self):
        return self.host_groups.all()

    def add_host_group(self, **kwargs):
        return self.host_groups.create(**kwargs)

    def add_var(self, **kwargs):
        return self.vars.create(**kwargs)

    def get_vars(self):
        return self.vars.all()

class InventoryVar(BaseVar):
    inventory = models.ForeignKey(Inventory, related_name='vars') 
    class Meta:
        unique_together = ('inventory', 'key')


class HostGroup(MPTTModel):
    inventory = models.ForeignKey('Inventory', related_name='host_groups')
    parent = TreeForeignKey('self', related_name='children', null=True, blank=True)
    name = models.CharField(_(u'name'), max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['parent__name', 'name',]
        unique_together = ('name', 'parent', 'inventory')
        verbose_name = _('host_group',)
        verbose_name_plural = _('host_groups',)

    def __unicode__(self):
        return "%s" % self.name

    def add_child_group(self, group):
        return self.children.add(group)

    def add_host(self, **kwargs):
        return self.hosts.create(inventory=self.inventory, **kwargs)
        
    def get_hosts(self):
        return self.hosts.all()

    def add_var(self, **kwargs):
        return self.vars.create(**kwargs)

    def get_vars(self):
        return self.vars.all()


class HostGroupVar(BaseVar):
    host_group = models.ForeignKey(HostGroup, related_name='vars')
    class Meta:
        unique_together = ('host_group', 'key')
 

class Host(models.Model):
    inventory = models.ForeignKey('Inventory', related_name='hosts')
    groups = models.ManyToManyField('HostGroup', related_name='hosts', blank=True, null=True)
    name = models.TextField()
    port = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    def add_group(self, group):
        return self.groups.add(group)

    def get_groups(self):
        return self.groups.all()

    def add_var(self, **kwargs):
        return self.vars.create(**kwargs)

    def get_vars(self):
        return self.vars.all()


class HostVar(BaseVar):
    host = models.ForeignKey(Host, related_name='vars')
    class Meta:
        unique_together = ('host', 'key')

