from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings

UNSET_ATTRIBUTE_VALUE_TEXT = getattr(settings, 'UNSET_ATTRIBUTE_VALUE_TEXT', "Not set")

class Inventory(models.Model):
    name = models.CharField(_('name'), max_length=40, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    def get_hosts(self):
        return self.hosts.all()

    def get_groups(self):
        return self.host_groups.all()


class HostGroup(models.Model):
    inventory = models.ForeignKey('Inventory', related_name='host_groups', null=True, blank=True)
    name = models.CharField(_(u'name'), max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        unique_together = ('name', 'inventory')
        verbose_name = _('host_group',)
        verbose_name_plural = _('host_groups',)

    def __unicode__(self):
        return "%s" % self.name

    def add_host(self, **kwargs):
        pass

    def get_hosts(self):
        pass

class Host(models.Model):
    inventory = models.ForeignKey('Inventory', related_name='hosts', null=True, blank=True)
    hostname = models.CharField(max_length=255, null=True, blank=True)
    ipaddress = models.GenericIPAddressField(protocol='IPv4')
    port = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def get_hostname(self):
        if self.hostname:
            return "%s - %s" % (self.hostname, self.ipaddress)
        else:
            return self.ipaddress

    def __unicode__(self):
        return "%s" % self.get_hostname()


class KVAttribute(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    class Meta:
        abstract = True
    
    def __unicade__(self):
        return "%s: %s" % (self.key, self.value or UNSET_ATTRIBUTE_VALUE_TEXT)

class HostAttribute(KVAttribute):
    host = models.ForeignKey(Host, related_name='vars')


class HostGroupAttribute(KVAttribute):
    host_group = models.ForeignKey(HostGroup, related_name='vars')


class InventoryAttribute(KVAttribute):
    inventory = models.ForeignKey(Inventory, related_name='vars')
