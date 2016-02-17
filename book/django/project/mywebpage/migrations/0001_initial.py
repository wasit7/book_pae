# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('std_id', models.IntegerField()),
                ('std_name', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('province_id', models.IntegerField()),
                ('sch_gpa', models.FloatField()),
                ('admit_year', models.CharField(max_length=8)),
            ],
        ),
    ]
