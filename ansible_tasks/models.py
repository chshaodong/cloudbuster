from django.db import models
from ansible_modules.models import AnsibleModule
from taggit.managers import TaggableManager

class Task(models.Model):
    name = models.CharField(max_length=40, unique=True)
    module = models.ForeignKey(AnsibleModule, null=True, blank=True)
    notify = models.ManyToManyField('self', null=True, blank=True)
    register = models.TextField(blank=True, null=True)
    environment = models.TextField(blank=True, null=True)
    remote_user = models.CharField(max_length=40, blank=True, null=True)
    sudo_user = models.CharField(max_length=40, blank=True, null=True)
    sudo_pass = models.CharField(max_length=255, blank=True, null=True)
    su_user = models.CharField(max_length=40, blank=True, null=True)
    su_pass = models.CharField(max_length=255, blank=True, null=True)
    sudo = models.BooleanField(default=False)
    su = models.BooleanField(default=False)
    no_log = models.BooleanField(default=False)
    inactive = models.BooleanField(default=False)
    local_action = models.BooleanField(default=False) 
    tags = TaggableManager(blank=True)
    is_handler = models.BooleanField(default=False)


class ModuleArgs(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    task = models.ForeignKey(Task, related_name='module_args')

    class Meta:
        unique_together = ('task', 'name')


