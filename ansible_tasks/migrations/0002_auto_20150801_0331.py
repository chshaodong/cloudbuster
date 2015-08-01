# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ansible_tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleArgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('task', models.ForeignKey(related_name='module_args', to='ansible_tasks.Task')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='moduleargs',
            unique_together=set([('task', 'name')]),
        ),
        migrations.RemoveField(
            model_name='task',
            name='module_args',
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
        ),
    ]
