# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-12 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
