# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebpage', '0002_auto_20160209_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.FloatField()),
                ('term', models.IntegerField()),
                ('year', models.IntegerField()),
                ('std_id', models.ForeignKey(to='mywebpage.Student')),
                ('sub_id', models.ForeignKey(to='mywebpage.Subject')),
            ],
        ),
    ]
