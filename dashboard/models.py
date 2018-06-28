# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime
from django.utils import timezone


@python_2_unicode_compatible  # only if you need to support Python 2
class Project(models.Model):
        #requester = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Requester")
        id = models.AutoField(primary_key=True)
        requester = models.CharField(blank=True,max_length=30)
        status = models.CharField(blank=True,max_length=30)
        project_name = models.CharField(blank=True,max_length=30,unique=True)
        application_name = models.CharField(blank=True,max_length=30)
        git_url = models.CharField(blank=True,max_length=256)
        UBUNTU_VERSION = models.CharField(blank=True,max_length=256)
        PHP_VERSION = models.CharField(blank=True,max_length=256)
        PHP_MODULES = models.CharField(blank=True,max_length=256)
        NGINX_BACKEND_HOST = models.CharField(blank=True,max_length=100)
        NGINX_BACKEND_HOST_VALUE = models.CharField(blank=True,max_length=500)
        NGINX_SERVER_NAME = models.CharField(blank=True,max_length=100)
        NGINX_SERVER_NAME_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_SERVER_ROOT = models.CharField( blank=True,max_length=100)
        NGINX_SERVER_ROOT_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_STATIC_CONTENT_ACCESS_LOG = models.CharField( blank=True,max_length=100)
        NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_STATIC_CONTENT_EXPIRES = models.CharField(blank=True,max_length=100)
        NGINX_STATIC_CONTENT_EXPIRES_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_DRUPAL_FILE_PROXY_URL = models.CharField(blank=True,max_length=100)
        NGINX_DRUPAL_FILE_PROXY_URL_VALUE = models.CharField( blank=True,max_length=500)
        MONGO_PORT_VALUE = models.CharField( blank=True,max_length=500)
        MONGO_INIT_DATABASE_VALUE = models.CharField( blank=True,max_length=500)
        MONGO_INITDB_ROOT_USERNAME_VALUE = models.CharField( blank=True,max_length=500)
        MONGO_INITDB_ROOT_PASSWORD_VALUE = models.CharField( blank=True,max_length=500)
        mongo_version = models.CharField( blank=True,max_length=500)
        class Meta:
                permissions = (
                    ('view_content', 'View content'),
                 )

        def __str__(self):
                return self.project_name
class RequestForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['project_flag','pub_date',]
        fields = ['requester', 'project_name','status', 'application_name' , 'git_url','UBUNTU_VERSION','PHP_VERSION','PHP_MODULES','NGINX_BACKEND_HOST','NGINX_BACKEND_HOST_VALUE','NGINX_SERVER_NAME','NGINX_SERVER_NAME_VALUE','NGINX_SERVER_ROOT','NGINX_SERVER_ROOT_VALUE','NGINX_STATIC_CONTENT_ACCESS_LOG','NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE','NGINX_STATIC_CONTENT_EXPIRES','NGINX_STATIC_CONTENT_EXPIRES_VALUE','NGINX_DRUPAL_FILE_PROXY_URL','NGINX_DRUPAL_FILE_PROXY_URL_VALUE',]
# Create your models here.
