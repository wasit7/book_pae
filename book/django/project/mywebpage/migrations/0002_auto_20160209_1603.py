# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_id', models.CharField(max_length=5)),
                ('sub_name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
                ('credit', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='birthdate',
        ),
    ]
