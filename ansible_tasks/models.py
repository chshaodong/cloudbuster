from django.db import models
from ansible_modules.models import AnsibleModule

class Task(models.Model):
    name = models.CharField(max_length=40)
    module = models.ForeignKey(AnsibleModule, null=True, blank=True)
    module_args = models.TextField(blank=True, null=True)
    notify = models.ManyToMany('self', null=True, blank=True)
    # tags = not yet implemented
    register = models.TextField(blank=True, null=True)
    local_action = models.BooleanField(default=False) 
    remote_user = models.CharField(max_length=40, blank=True, null=True)
    sudo = models.BooleanField(default=False)
    sudo_user = models.CharField(max_length=40, blank=True, null=True)
    sudo_pass = models.CharField(max_length=255, blank=True, null=True)
    environment = models.TextField(blank=True, null=True)
    su = models.BooleanField(default=False)
    su_user = models.CharField(max_length=40, blank=True, null=True)
    su_pass = models.CharField(max_length=255, blank=True, null=True)
    no_log = models.BooleanField(default=False)
    is_handler = models.BooleanField(default=False)

