# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='runningstack',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('projectname', models.CharField(max_length=50, blank=True)),
                ('status', models.CharField(max_length=50, blank=True)),
                ('url', models.CharField(max_length=50, blank=True)),
                ('urlStatus', models.CharField(max_length=50, blank=True)),
                ('hostIp', models.CharField(max_length=50, blank=True)),
                ('hostStatus', models.CharField(max_length=50, blank=True)),
                ('nginxport', models.CharField(max_length=50, blank=True)),
                ('varnishport', models.CharField(max_length=50, blank=True)),
                ('mysqluname', models.CharField(max_length=50, blank=True)),
                ('mysqlupwd', models.CharField(max_length=50, blank=True)),
                ('mysqlstatus', models.CharField(max_length=50, blank=True)),
                ('mongouname', models.CharField(max_length=50, blank=True)),
                ('mongoupwd', models.CharField(max_length=50, blank=True)),
                ('mongostatus', models.CharField(max_length=50, blank=True)),
            ],
        ),
    ]
