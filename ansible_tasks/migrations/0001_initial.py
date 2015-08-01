# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('ansible_modules', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('module_args', models.TextField(null=True, blank=True)),
                ('register', models.TextField(null=True, blank=True)),
                ('environment', models.TextField(null=True, blank=True)),
                ('remote_user', models.CharField(max_length=40, null=True, blank=True)),
                ('sudo_user', models.CharField(max_length=40, null=True, blank=True)),
                ('sudo_pass', models.CharField(max_length=255, null=True, blank=True)),
                ('su_user', models.CharField(max_length=40, null=True, blank=True)),
                ('su_pass', models.CharField(max_length=255, null=True, blank=True)),
                ('sudo', models.BooleanField(default=False)),
                ('su', models.BooleanField(default=False)),
                ('no_log', models.BooleanField(default=False)),
                ('inactive', models.BooleanField(default=False)),
                ('local_action', models.BooleanField(default=False)),
                ('is_handler', models.BooleanField(default=False)),
                ('module', models.ForeignKey(blank=True, to='ansible_modules.AnsibleModule', null=True)),
                ('notify', models.ManyToManyField(related_name='notify_rel_+', null=True, to='ansible_tasks.Task', blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
