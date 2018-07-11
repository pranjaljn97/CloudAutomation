# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_runningstack'),
    ]

    operations = [
        migrations.AddField(
            model_name='ports',
            name='ptype',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
