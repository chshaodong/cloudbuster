from django.db import models

class AnsibleModule(models.Model):
    description = models.TextField(blank=True)
    module = models.CharField(max_length=140,blank=True)
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

class AnsibleModuleOption(models.Model):
    module = models.ForeignKey(AnsibleModule, related_name='options')
    name = models.CharField(max_length=40,blank=True)
    default = models.CharField(max_length=40, blank=True)
    required = models.CharField(max_length=20,blank=True)
    description = models.TextField(blank=True)
    choices = models.TextField(blank=True)
    aliases = models.TextField(blank=True)

    def get_fields(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, values

