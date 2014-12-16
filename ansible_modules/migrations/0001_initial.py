# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnsibleModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('module', models.CharField(max_length=140)),
                ('option_keys', models.TextField()),
                ('docuri', models.CharField(max_length=140)),
                ('requirements', models.TextField()),
                ('author', models.CharField(max_length=140)),
                ('filename', models.TextField()),
                ('version_added', models.CharField(max_length=140)),
                ('short_description', models.TextField()),
                ('options', models.TextField()),
                ('module_path', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
