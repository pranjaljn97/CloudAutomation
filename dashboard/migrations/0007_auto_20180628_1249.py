# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-28 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20171007_2024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': (('view_content', 'View content'),)},
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value1',
            new_name='MONGO_INITDB_ROOT_PASSWORD_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value10',
            new_name='MONGO_INITDB_ROOT_USERNAME_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value2',
            new_name='MONGO_INIT_DATABASE_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value3',
            new_name='MONGO_PORT_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value4',
            new_name='NGINX_BACKEND_HOST_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value5',
            new_name='NGINX_DRUPAL_FILE_PROXY_URL_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value6',
            new_name='NGINX_SERVER_NAME_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value7',
            new_name='NGINX_SERVER_ROOT_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value8',
            new_name='NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='env_value9',
            new_name='NGINX_STATIC_CONTENT_EXPIRES_VALUE',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='build_tool',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key10',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key3',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key4',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key5',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key6',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key7',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key8',
        ),
        migrations.RemoveField(
            model_name='project',
            name='env_key9',
        ),
        migrations.RemoveField(
            model_name='project',
            name='git_branch',
        ),
        migrations.RemoveField(
            model_name='project',
            name='jenkins_status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='project',
            name='mongo_password',
        ),
        migrations.RemoveField(
            model_name='project',
            name='mongo_status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='mysql_password',
        ),
        migrations.RemoveField(
            model_name='project',
            name='mysql_status',
        ),
        migrations.RemoveField(
            model_name='project',
            name='platform_version',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_flag',
        ),
        migrations.RemoveField(
            model_name='project',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='project',
            name='NGINX_BACKEND_HOST',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='NGINX_DRUPAL_FILE_PROXY_URL',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='NGINX_SERVER_NAME',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='NGINX_SERVER_ROOT',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='NGINX_STATIC_CONTENT_ACCESS_LOG',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='NGINX_STATIC_CONTENT_EXPIRES',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='PHP_MODULES',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='project',
            name='PHP_VERSION',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='project',
            name='UBUNTU_VERSION',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='project',
            name='mongo_version',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='application_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='git_url',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='requester',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
