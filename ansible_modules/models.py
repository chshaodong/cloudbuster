from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from ansible_modules.managers import ModuleCategoryManager
from mptt.models import MPTTModel, TreeForeignKey

class ModuleCategory(MPTTModel):
    parent = TreeForeignKey('self', null=True, related_name='subcategories')
    name = models.CharField(_(u'name'), max_length=40)
    slug = models.TextField(max_length=255, blank=True)

    objects = ModuleCategoryManager()
    
    class Meta:
        ordering = ['parent__name', 'name',]
        unique_together = ('slug', 'parent',)
        verbose_name = _('module_category',)
        verbose_name_plural = _('module_categories',)

    def get_fields(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, values

    def __str__(self):
        return "%s" % self.slug


class AnsibleModule(models.Model):
    module_category = models.ForeignKey("ModuleCategory", related_name='modules', null=True, blank=True)
    description = models.TextField(blank=True)
    module = models.CharField(_(u'name'), max_length=140,blank=True)
    option_keys = models.TextField(blank=True)
    docuri = models.CharField(max_length=140,blank=True)           
    requirements = models.TextField(blank=True)
    author = models.CharField(max_length=140,blank=True)
    filename = models.TextField(blank=True)        
    version_added = models.CharField(max_length=140,blank=True)
    short_description = models.TextField(blank=True)
    module_path = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_fields(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value  

    def __str__(self):
        return "%s - %s" % (self.module, self.module_path)

class AnsibleModuleOption(models.Model):
    module = models.ForeignKey(AnsibleModule, related_name='options')
    name = models.CharField(_(u'name'), max_length=40,blank=True)
    default = models.CharField(max_length=40, blank=True)
    required = models.CharField(max_length=20,blank=True)
    description = models.TextField(blank=True)
    choices = models.TextField(blank=True)
    aliases = models.TextField(blank=True)

    def get_fields(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, values

