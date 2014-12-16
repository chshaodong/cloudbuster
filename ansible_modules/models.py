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
    options = models.TextField(blank=True)
    module_path = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


