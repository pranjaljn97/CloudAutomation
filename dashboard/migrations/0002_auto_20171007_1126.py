# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='cpu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='memory',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
