# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebpage', '0003_enrollment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='std_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sub_id',
            field=models.CharField(max_length=5, serialize=False, primary_key=True),
        ),
    ]
