# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime
from django import forms
from django.utils import timezone
import os




    
class Ports(models.Model):
    id = models.AutoField(primary_key=True)
    port = models.CharField(blank=True, max_length=30)
    status = models.CharField(blank=True, max_length=30)
    projectname = models.CharField(blank=True, max_length=30)
    ptype = models.CharField(blank=True, max_length=30)

    def __str__(self):
          return self.projectname

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

    def __str__(self):
          return self.projectname


class status(models.Model):
    id = models.AutoField(primary_key=True)
    projectname = models.CharField(blank=True, max_length=1000)
    sshstatus = models.CharField(blank=True, max_length=1000)
    dockerstatus = models.CharField(blank=True, max_length=1000)
    urlstatus = models.CharField(blank=True, max_length=1000)
    mongostatus = models.CharField(blank=True, max_length=1000)
    mysqlstatus = models.CharField(blank=True, max_length=1000)
    nginxstatus = models.CharField(blank=True, max_length=1000)
    varnishstatus = models.CharField(blank=True, max_length=1000)
    redisstatus = models.CharField(blank=True, max_length=1000)
    mysqlid = models.CharField(blank=True, max_length=1000)
    mysqlname = models.CharField(blank=True, max_length=1000)
    mysqlst = models.CharField(blank=True, max_length=1000)
    mongoid = models.CharField(blank=True, max_length=1000)
    mongoname = models.CharField(blank=True, max_length=1000)
    mongost = models.CharField(blank=True, max_length=1000)
    varnishid = models.CharField(blank=True, max_length=1000)
    varnishname = models.CharField(blank=True, max_length=1000)
    varnishst = models.CharField(blank=True, max_length=1000)
    nginxid = models.CharField(blank=True, max_length=1000)
    nginxname = models.CharField(blank=True, max_length=1000)
    nginxst = models.CharField(blank=True, max_length=1000)
    redisid = models.CharField(blank=True, max_length=1000)
    redisname = models.CharField(blank=True, max_length=1000)
    redisst = models.CharField(blank=True, max_length=1000)

class hoststatus(models.Model):
    id = models.AutoField(primary_key=True)
    sshstatus = models.CharField(blank=True, max_length=1000)
    dockerstatus = models.CharField(blank=True, max_length=1000)
    mongostatus = models.CharField(blank=True, max_length=1000)
    mysqlstatus = models.CharField(blank=True, max_length=1000)




    
class Host(models.Model):
        id = models.AutoField(primary_key=True)
        hostIdentifier = models.CharField(blank=True, max_length=30)
        hostIp = models.CharField(blank=True, max_length=30, unique=True)
        hostUsername = models.CharField(blank=True,max_length=30)
        hostPassword = models.CharField(blank=True,max_length=30)
        status = models.CharField(default='initiated', max_length=30)
        hostDocker = models.CharField(blank=True,max_length=30)
        hostNginx = models.CharField(blank=True,max_length=30)
        hostMysql = models.CharField(blank=True,max_length=30)
        hostMongo = models.CharField(blank=True,max_length=30)
        mysqlUsername = models.CharField(blank=True,max_length=50)
        mysqlPassword = models.CharField(blank=True,max_length=50)
        mongoUsername = models.CharField(blank=True,max_length=50)
        mongoPassword = models.CharField(blank=True,max_length=50)
        class Meta:
                permissions = (
                    ('view_content', 'View content'),
                 )
        def __str__(self):
          return self.hostIdentifier

       
       


class HostForm(ModelForm):
    class Meta:
        model = Host
        fields = ['hostIdentifier','hostIp','hostUsername','hostPassword','hostDocker','hostNginx','hostMysql','hostMongo','mysqlUsername','mysqlPassword','mongoUsername', 'mongoPassword']



def unique_file_path(instance, filename):
    return 'documents/{0}/{1}'.format(instance.project_name, filename)

class Project(models.Model):
        
        #requester = models.ForeignKey(User,default=1)
        #===#=================step 1 (basic details)=====================================
        #requester = models.ForeignKey(settings.AUTH_USER_MODEL)

        requester = models.CharField(blank=True,max_length=100)
        id = models.AutoField(primary_key=True)
        #requester = models.CharField(blank=True,max_length=100)

        platform = models.CharField(blank=True,max_length=30)
        hostIp = models.CharField(blank=True, max_length=30)
        hostIp_mysql = models.CharField(blank=True, max_length=30)
        legacy1 = models.CharField(default='Yes', max_length=30)
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
        document = models.FileField(upload_to=unique_file_path,blank=True)
        # NGINX_BACKEND_HOST_VALUE = models.CharField(blank=True,max_length=500)
        # NGINX_SERVER_NAME_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_SERVER_ROOT_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE = models.CharField( blank=True,max_length=500)
        NGINX_STATIC_CONTENT_EXPIRES_VALUE = models.CharField( blank=True,max_length=500)

        #==================Extra Key Value Pairs============================================
        total = models.CharField( blank=True,max_length=100)
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
        fields = ['requester','platform','envtype', 'project_name', 'application_name' ,'hostIp','repo_type', 'git_url','git_token','git_username','git_branch','UBUNTU_VERSION','PHP_VERSION','PHP_MODULES','document','NGINX_SERVER_ROOT_VALUE','NGINX_STATIC_CONTENT_ACCESS_LOG_VALUE','NGINX_STATIC_CONTENT_EXPIRES_VALUE','total','key1','value1','key2','value2','key3','value3','key4','value4','key5','value5','mysql_version','MYSQL_DATABASE_NAME_VALUE','MYSQL_ROOT_PASSWORD_VALUE','MYSQL_USER_NAME_VALUE','MYSQL_PASSWORD_VALUE','MYSQL_CLIENT_DEFAULT_CHARACTER_SET_VALUE','MONGO_INITDB_DATABASE_VALUE','MONGO_INITDB_ROOT_USERNAME_VALUE','MONGO_INITDB_ROOT_PASSWORD_VALUE','mongo_version','varnish_version','VARNISH_BACKEND_HOST_VALUE','VARNISH_BACKEND_PORT_VALUE','VARNISH_PORT_VALUE','redis_version','REDIS_PASSWORD_VALUE', ]

class Myform(forms.Form):
    newbranch = forms.CharField(required=False,max_length=40)
    total = forms.CharField(required=False,max_length=40)
    key1 = forms.CharField(required=False,max_length=40)
    value1 = forms.CharField(required=False,max_length=40)
    key2 = forms.CharField(required=False,max_length=40)
    value2 = forms.CharField(required=False,max_length=40)
    key3 = forms.CharField(required=False,max_length=40)
    value3 = forms.CharField(required=False,max_length=40)
    key4 = forms.CharField(required=False,max_length=40)
    value4 = forms.CharField(required=False,max_length=40)
    key5 = forms.CharField(required=False,max_length=40)
    value5 = forms.CharField(required=False,max_length=40)
    key6 = forms.CharField(required=False,max_length=40)
    value6 = forms.CharField(required=False,max_length=40)
    key7 = forms.CharField(required=False,max_length=40)
    value7 = forms.CharField(required=False,max_length=40)
    key8 = forms.CharField(required=False,max_length=40)
    value8 = forms.CharField(required=False,max_length=40)
    key9 = forms.CharField(required=False,max_length=40)
    value9 = forms.CharField(required=False,max_length=40)
    key10 = forms.CharField(required=False,max_length=40)
    value10 = forms.CharField(required=False,max_length=40)

class mysqluser(models.Model):
        requester = models.CharField(blank=True,max_length=100)
        id = models.AutoField(primary_key=True)
        hostIp = models.CharField(blank=True, max_length=30)
        MYSQL_DATABASE_NAME_VALUE = models.CharField( blank=True,max_length=100)
        MYSQL_USER_NAME_VALUE = models.CharField( blank=True,max_length=100)
        MYSQL_PASSWORD_VALUE = models.CharField( blank=True,max_length=100)
        status = models.CharField(default='submitted', max_length=30)
        def __str__(self):
          return self.requester
        
class mysqlForm(ModelForm):
    class Meta:
        model = mysqluser
        fields = ['requester','hostIp','MYSQL_DATABASE_NAME_VALUE','MYSQL_USER_NAME_VALUE','MYSQL_PASSWORD_VALUE',]


class mongoform(models.Model):
    requester = models.CharField(blank=True,max_length=100)
    id = models.AutoField(primary_key=True)
    hostip = models.CharField( blank=True,max_length=500)
    MONGO_INITDB_DATABASE_VALUE = models.CharField( blank=True,max_length=500)
    MONGO_INITDB_ROOT_USERNAME_VALUE = models.CharField( blank=True,max_length=500)
    MONGO_INITDB_ROOT_PASSWORD_VALUE = models.CharField( blank=True,max_length=500)
    status = models.CharField(default='submitted', max_length=30)
    def __str__(self):
          return self.requester
    
class mongorequest(ModelForm):
    class Meta:
        model = mongoform
        fields = ['requester','hostip','MONGO_INITDB_DATABASE_VALUE','MONGO_INITDB_ROOT_USERNAME_VALUE', 'MONGO_INITDB_ROOT_PASSWORD_VALUE',]


class hostdeploy(models.Model):
    id = models.AutoField(primary_key=True)
    hostipdeploy = models.CharField( blank=True,max_length=500)
    hostiplegacy = models.CharField( blank=True,max_length=500)

class HostdeployForm(ModelForm):
    class Meta:
        model = hostdeploy
        fields = ['hostipdeploy','hostiplegacy']

    
    
    


