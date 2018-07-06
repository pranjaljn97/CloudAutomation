# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('hostIdentifier', models.CharField(max_length=30, blank=True)),
                ('hostIp', models.CharField(max_length=30, blank=True)),
                ('hostUsername', models.CharField(max_length=30, blank=True)),
                ('hostPassword', models.CharField(max_length=30, blank=True)),
                ('status', models.CharField(default='initiated', max_length=30)),
            ],
            options={
                'permissions': (('view_content', 'View content'),),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('requester', models.CharField(max_length=100, blank=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('platform', models.CharField(max_length=30, blank=True)),
                ('hostIp', models.CharField(max_length=30, blank=True)),
                ('envtype', models.CharField(max_length=30, blank=True)),
                ('project_name', models.CharField(unique=True, max_length=30, blank=True)),
                ('application_name', models.CharField(max_length=30, blank=True)),
                ('git_url', models.CharField(max_length=256, blank=True)),
                ('status', models.CharField(default='submitted', max_length=30)),
                ('UBUNTU_VERSION', models.CharField(max_length=256, blank=True)),
                ('PHP_VERSION', models.CharField(max_length=256, blank=True)),
                ('PHP_MODULES', models.CharField(max_length=256, blank=True)),
                ('NGINX_BACKEND_HOST_VALUE', models.CharField(max_length=500, blank=True)),
                ('NGINX_SERVER_NAME_VALUE', models.CharField(max_length=500, blank=True)),
                ('NGINX_SERVER_ROOT_VALUE', models.CharField(max_length=500, blank=True)),
                ('NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE', models.CharField(max_length=500, blank=True)),
                ('NGINX_STATIC_CONTENT_EXPIRES_VALUE', models.CharField(max_length=500, blank=True)),
                ('key1', models.CharField(max_length=100, blank=True)),
                ('value1', models.CharField(max_length=100, blank=True)),
                ('key2', models.CharField(max_length=100, blank=True)),
                ('value2', models.CharField(max_length=100, blank=True)),
                ('key3', models.CharField(max_length=100, blank=True)),
                ('value3', models.CharField(max_length=100, blank=True)),
                ('key4', models.CharField(max_length=100, blank=True)),
                ('value4', models.CharField(max_length=100, blank=True)),
                ('key5', models.CharField(max_length=100, blank=True)),
                ('value5', models.CharField(max_length=100, blank=True)),
                ('MONGO_PORT_VALUE', models.CharField(max_length=500, blank=True)),
                ('MONGO_INITDB_DATABASE_VALUE', models.CharField(max_length=500, blank=True)),
                ('MONGO_INITDB_ROOT_USERNAME_VALUE', models.CharField(max_length=500, blank=True)),
                ('MONGO_INITDB_ROOT_PASSWORD_VALUE', models.CharField(max_length=500, blank=True)),
                ('mongo_version', models.CharField(max_length=500, blank=True)),
                ('mysql_version', models.CharField(max_length=20, blank=True)),
                ('MYSQL_DATABASE_NAME_VALUE', models.CharField(max_length=100, blank=True)),
                ('MYSQL_ROOT_PASSWORD_VALUE', models.CharField(max_length=100, blank=True)),
                ('MYSQL_USER_NAME_VALUE', models.CharField(max_length=100, blank=True)),
                ('MYSQL_PASSWORD_VALUE', models.CharField(max_length=100, blank=True)),
                ('MYSQL_PORT_VALUE', models.CharField(max_length=100, blank=True)),
                ('MYSQL_CLIENT_DEFAULT_CHARACTER_SET_VALUE', models.CharField(max_length=100, blank=True)),
                ('MYSQL_DUMP_MAX_ALLOWED_PACKET', models.CharField(max_length=100, blank=True)),
                ('varnish_version', models.CharField(max_length=100, blank=True)),
                ('VARNISH_BACKEND_HOST_VALUE', models.CharField(max_length=100, blank=True)),
                ('VARNISH_BACKEND_PORT_VALUE', models.CharField(max_length=100, blank=True)),
                ('VARNISH_PORT_VALUE', models.CharField(max_length=100, blank=True)),
                ('redis_version', models.CharField(max_length=100, blank=True)),
                ('REDIS_PASSWORD_VALUE', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'permissions': (('view_content', 'View content'),),
            },
        ),
    ]
