# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime
from django.utils import timezone
class Project(models.Model):
        
        #requester = models.ForeignKey(User,default=1)
        #===#=================step 1 (basic details)=====================================
        #requester = models.ForeignKey(settings.AUTH_USER_MODEL)
	id = models.AutoField(primary_key=True)
        requester = models.CharField(blank=True,max_length=30)
        platform = models.CharField(blank=True,max_length=30)
        envtype = models.CharField(blank=True,max_length=30)
        project_name = models.CharField(blank=True,max_length=30,unique=True)
        application_name = models.CharField(blank=True,max_length=30)
        git_url = models.CharField(blank=True,max_length=256)
        status = models.CharField(blank=True,max_length=30)

        #=================step 2(php-nginx details)========================================
        UBUNTU_VERSION = models.CharField(blank=True,max_length=256)
        PHP_VERSION = models.CharField(blank=True,max_length=256)
        PHP_MODULES = models.CharField(blank=True,max_length=256)
        NGINX_BACKEND_HOST_VALUE = models.CharField(blank=True,max_length=500)
        NGINX_SERVER_NAME_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_SERVER_ROOT_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_STATIC_CONTENT_EXPIRES_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_DRUPAL_FILE_PROXY_URL_VALUE = models.CharField( blank=True,max_length=500)
        MONGO_PORT_VALUE = models.CharField( blank=True,max_length=500)
        MONGO_INITDB_DATABASE_VALUE = models.CharField( blank=True,max_length=500)
        MONGO_INITDB_ROOT_USERNAME_VALUE = models.CharField( blank=True,max_length=500)
        MONGO_INITDB_ROOT_PASSWORD_VALUE = models.CharField( blank=True,max_length=500)
        mongo_version = models.CharField( blank=True,max_length=500)


        #=====================step 3(mysql details)===============================================
        mysql_version = models.CharField( blank=True,max_length=20)
        MYSQL_DATABASE_NAME_VALUE = models.CharField( blank=True,max_length=100)
        MYSQL_ROOT_PASSWORD_VALUE = models.CharField( blank=True,max_length=100)
        MYSQL_USER_NAME_VALUE = models.CharField( blank=True,max_length=100)
        MYSQL_PASSWORD_VALUE = models.CharField( blank=True,max_length=100)
        MYSQL_PORT_VALUE = models.CharField( blank=True,max_length=100)
        MYSQL_CLIENT_DEFAULT_CHARACTER_SET_VALUE = models.CharField( blank=True,max_length=100)
        MYSQL_DUMP_MAX_ALLOWED_PACKET = models.CharField( blank=True,max_length=100)

        #===================step 4(varnish details)=============================================
        varnish_version = models.CharField( blank=True,max_length=100)
        VARNISH_BACKEND_HOST_VALUE = models.CharField( blank=True,max_length=100)
        VARNISH_BACKEND_PORT_VALUE = models.CharField( blank=True,max_length=100)
        VARNISH_PORT_VALUE = models.CharField( blank=True,max_length=100)

        #======================step 5(redis details)=========================================
        redis_version = models.CharField( blank=True,max_length=100)
        REDIS_PASSWORD_VALUE = models.CharField( blank=True,max_length=100)


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
        fields = ['requester','platform','envtype', 'project_name','status', 'application_name' , 'git_url','UBUNTU_VERSION','PHP_VERSION','PHP_MODULES','NGINX_BACKEND_HOST_VALUE','NGINX_SERVER_NAME_VALUE','NGINX_SERVER_ROOT_VALUE','NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE','NGINX_STATIC_CONTENT_EXPIRES_VALUE','NGINX_DRUPAL_FILE_PROXY_URL_VALUE','mysql_version','MYSQL_DATABASE_NAME_VALUE','MYSQL_ROOT_PASSWORD_VALUE','MYSQL_USER_NAME_VALUE','MYSQL_PASSWORD_VALUE','MYSQL_PORT_VALUE','MYSQL_CLIENT_DEFAULT_CHARACTER_SET_VALUE','MYSQL_DUMP_MAX_ALLOWED_PACKET','MONGO_PORT_VALUE','MONGO_INITDB_DATABASE_VALUE','MONGO_INITDB_ROOT_USERNAME_VALUE','MONGO_INITDB_ROOT_PASSWORD_VALUE','mongo_version','varnish_version','VARNISH_BACKEND_HOST_VALUE','VARNISH_BACKEND_PORT_VALUE','VARNISH_PORT_VALUE','redis_version','REDIS_PASSWORD_VALUE', ]
# Create your models here.,
