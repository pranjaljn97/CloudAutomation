# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime
from django.utils import timezone


class Ports(models.Model):
    id = models.AutoField(primary_key=True)
    port = models.CharField(blank=True, max_length=30)
    status = models.CharField(blank=True, max_length=30)
    projectname = models.CharField(blank=True, max_length=30)
    ptype = models.CharField(blank=True, max_length=30)

class runningstack(models.Model):
    id = models.AutoField(primary_key=True)
    projectname = models.CharField(blank=True, max_length=50)
    status = models.CharField(blank=True, max_length=50)
    url = models.CharField(blank=True, max_length=50)
    urlStatus = models.CharField(blank=True, max_length=50)
    hostIp = models.CharField(blank=True, max_length=50)
    hostStatus = models.CharField(blank=True, max_length=50)
    nginxport = models.CharField(blank=True, max_length=50)
    varnishport = models.CharField(blank=True, max_length=50)
    mysqluname = models.CharField(blank=True, max_length=50)
    mysqlupwd = models.CharField(blank=True, max_length=50)
    mysqlstatus = models.CharField(blank=True, max_length=50)
    mongouname = models.CharField(blank=True, max_length=50)
    mongoupwd = models.CharField(blank=True, max_length=50)
    mongostatus = models.CharField(blank=True, max_length=50)
    approvedBy = models.CharField(blank=True,max_length=256)


class Host(models.Model):
        id = models.AutoField(primary_key=True)
        hostIdentifier = models.CharField(blank=True, max_length=30)
        hostIp = models.CharField(blank=True, max_length=30)
        hostUsername = models.CharField(blank=True,max_length=30)
        hostPassword = models.CharField(blank=True,max_length=30)
        status = models.CharField(default='initiated', max_length=30)
        class Meta:
                permissions = (
                    ('view_content', 'View content'),
                 )

class HostForm(ModelForm):
    class Meta:
        model = Host
        fields = ['hostIdentifier','hostIp','hostUsername','hostPassword']

class Project(models.Model):
        
        #requester = models.ForeignKey(User,default=1)
        #===#=================step 1 (basic details)=====================================
        #requester = models.ForeignKey(settings.AUTH_USER_MODEL)

        requester = models.CharField(blank=True,max_length=100)
        id = models.AutoField(primary_key=True)
        #requester = models.CharField(blank=True,max_length=100)

        platform = models.CharField(blank=True,max_length=30)
        hostIp = models.CharField(blank=True, max_length=30)
        envtype = models.CharField(blank=True,max_length=30)
        project_name = models.CharField(blank=True,max_length=30,unique=True)
        application_name = models.CharField(blank=True,max_length=30)
        repo_type = models.CharField(blank=True,max_length=256)
        git_url = models.CharField(blank=True,max_length=256)
        git_token = models.CharField(blank=True,max_length=256)
        git_username = models.CharField(blank=True,max_length=256)
        git_branch = models.CharField(blank=True,max_length=256)
        status = models.CharField(default='submitted', max_length=30)
        approvedBy = models.CharField(blank=True,max_length=256)

        #=================step 2(php-nginx details)========================================
        UBUNTU_VERSION = models.CharField(blank=True,max_length=256)
        PHP_VERSION = models.CharField(blank=True,max_length=256)
        PHP_MODULES = models.CharField(blank=True,max_length=256)
        fileopp = models.CharField(blank=True,max_length=30)
        document = models.FileField(upload_to='documents/',blank=True)
        # NGINX_BACKEND_HOST_VALUE = models.CharField(blank=True,max_length=500)
        # NGINX_SERVER_NAME_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_SERVER_ROOT_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_STATIC_CONTENT_EXPIRES_VALUE = models.CharField( blank=True,max_length=500)

        #==================Extra Key Value Pairs============================================
        key1 = models.CharField( blank=True,max_length=100)
        value1 = models.CharField( blank=True,max_length=100)
        key2 = models.CharField( blank=True,max_length=100)
        value2 = models.CharField( blank=True,max_length=100)
        key3 = models.CharField( blank=True,max_length=100)
        value3 = models.CharField( blank=True,max_length=100)
        key4 = models.CharField( blank=True,max_length=100)
        value4 = models.CharField( blank=True,max_length=100)
        key5 = models.CharField( blank=True,max_length=100)
        value5 = models.CharField( blank=True,max_length=100)



        # MONGO_PORT_VALUE = models.CharField( blank=True,max_length=500)
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
        # MYSQL_PORT_VALUE = models.CharField( blank=True,max_length=100)
        MYSQL_CLIENT_DEFAULT_CHARACTER_SET_VALUE = models.CharField( blank=True,max_length=100)
        # MYSQL_DUMP_MAX_ALLOWED_PACKET = models.CharField( blank=True,max_length=100)

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
        fields = ['requester','platform','envtype', 'project_name', 'application_name' ,'hostIp','repo_type', 'git_url','git_token','git_username','git_branch','UBUNTU_VERSION','PHP_VERSION','PHP_MODULES','document','NGINX_SERVER_ROOT_VALUE','NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE','NGINX_STATIC_CONTENT_EXPIRES_VALUE','key1','value1','key2','value2','key3','value3','key4','value4','key5','value5','mysql_version','MYSQL_DATABASE_NAME_VALUE','MYSQL_ROOT_PASSWORD_VALUE','MYSQL_USER_NAME_VALUE','MYSQL_PASSWORD_VALUE','MYSQL_CLIENT_DEFAULT_CHARACTER_SET_VALUE','MONGO_INITDB_DATABASE_VALUE','MONGO_INITDB_ROOT_USERNAME_VALUE','MONGO_INITDB_ROOT_PASSWORD_VALUE','mongo_version','varnish_version','VARNISH_BACKEND_HOST_VALUE','VARNISH_BACKEND_PORT_VALUE','VARNISH_PORT_VALUE','redis_version','REDIS_PASSWORD_VALUE', ]
