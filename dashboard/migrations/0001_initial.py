# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-07-09 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hostIdentifier', models.CharField(blank=True, max_length=30)),
                ('hostIp', models.CharField(blank=True, max_length=30)),
                ('hostUsername', models.CharField(blank=True, max_length=30)),
                ('hostPassword', models.CharField(blank=True, max_length=30)),
                ('status', models.CharField(default='initiated', max_length=30)),
            ],
            options={
                'permissions': (('view_content', 'View content'),),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('requester', models.CharField(blank=True, max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('platform', models.CharField(blank=True, max_length=30)),
                ('hostIp', models.CharField(blank=True, max_length=30)),
                ('envtype', models.CharField(blank=True, max_length=30)),
                ('project_name', models.CharField(blank=True, max_length=30, unique=True)),
                ('application_name', models.CharField(blank=True, max_length=30)),
                ('git_url', models.CharField(blank=True, max_length=256)),
                ('git_token', models.CharField(blank=True, max_length=256)),
                ('git_username', models.CharField(blank=True, max_length=256)),
                ('git_branch', models.CharField(blank=True, max_length=256)),
                ('status', models.CharField(default='submitted', max_length=30)),
                ('UBUNTU_VERSION', models.CharField(blank=True, max_length=256)),
                ('PHP_VERSION', models.CharField(blank=True, max_length=256)),
                ('PHP_MODULES', models.CharField(blank=True, max_length=256)),
                ('NGINX_SERVER_ROOT_VALUE', models.CharField(blank=True, max_length=500)),
                ('NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE', models.CharField(blank=True, max_length=500)),
                ('NGINX_STATIC_CONTENT_EXPIRES_VALUE', models.CharField(blank=True, max_length=500)),
                ('key1', models.CharField(blank=True, max_length=100)),
                ('value1', models.CharField(blank=True, max_length=100)),
                ('key2', models.CharField(blank=True, max_length=100)),
                ('value2', models.CharField(blank=True, max_length=100)),
                ('key3', models.CharField(blank=True, max_length=100)),
                ('value3', models.CharField(blank=True, max_length=100)),
                ('key4', models.CharField(blank=True, max_length=100)),
                ('value4', models.CharField(blank=True, max_length=100)),
                ('key5', models.CharField(blank=True, max_length=100)),
                ('value5', models.CharField(blank=True, max_length=100)),
                ('MONGO_INITDB_DATABASE_VALUE', models.CharField(blank=True, max_length=500)),
                ('MONGO_INITDB_ROOT_USERNAME_VALUE', models.CharField(blank=True, max_length=500)),
                ('MONGO_INITDB_ROOT_PASSWORD_VALUE', models.CharField(blank=True, max_length=500)),
                ('mongo_version', models.CharField(blank=True, max_length=500)),
                ('mysql_version', models.CharField(blank=True, max_length=20)),
                ('MYSQL_DATABASE_NAME_VALUE', models.CharField(blank=True, max_length=100)),
                ('MYSQL_ROOT_PASSWORD_VALUE', models.CharField(blank=True, max_length=100)),
                ('MYSQL_USER_NAME_VALUE', models.CharField(blank=True, max_length=100)),
                ('MYSQL_PASSWORD_VALUE', models.CharField(blank=True, max_length=100)),
                ('MYSQL_CLIENT_DEFAULT_CHARACTER_SET_VALUE', models.CharField(blank=True, max_length=100)),
                ('varnish_version', models.CharField(blank=True, max_length=100)),
                ('VARNISH_BACKEND_HOST_VALUE', models.CharField(blank=True, max_length=100)),
                ('VARNISH_BACKEND_PORT_VALUE', models.CharField(blank=True, max_length=100)),
                ('VARNISH_PORT_VALUE', models.CharField(blank=True, max_length=100)),
                ('redis_version', models.CharField(blank=True, max_length=100)),
                ('REDIS_PASSWORD_VALUE', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'permissions': (('view_content', 'View content'),),
            },
        ),
    ]
