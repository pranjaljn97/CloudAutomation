# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-29 11:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20180629_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='requester',
            field=models.ForeignKey(db_column='username', default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
