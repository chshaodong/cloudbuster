from django.db import models
from ansible_tasks.models import Task
from inventory.models import Inventory

class Play(models.Model):
    name = models.CharField(max_length=140)
    hosts = models.TextField(null=True, blank=True)
    tasks = models.ManyToManyField(Task, related_name='in_plays', through='TaskList')
    remote_user = models.CharField(max_length=40, blank=True, null=True)
    sudo = models.BooleanField(default=False)
    sudo_user = models.CharField(max_length=40, blank=True, null=True)
    sudo_pass = models.CharField(max_length=255, blank=True, null=True)
    environment = models.TextField(blank=True, null=True)
    su = models.BooleanField(default=False)
    su_user = models.CharField(max_length=40, blank=True, null=True)
    su_pass = models.CharField(max_length=255, blank=True, null=True)    
    
class TaskList(models.Model):
    number = models.PositiveIntegerField()
    play = models.ForeignKey(Play)
    task = models.ForeignKey(Task)


class Playbook(models.Model):
    """A collection of Plays"""
    name = models.CharField(max_length=140)
    plays = models.ManyToManyField(Play, related_name='in_playbook', through='PlayList')


class PlayList(models.Model):
   number = models.PositiveIntegerField()
   playbook = models.ForeignKey(Playbook)
   play = models.ForeignKey(Play) 

   
