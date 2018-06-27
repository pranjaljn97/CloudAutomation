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
	requester = models.CharField(max_length=30)
	project_name = models.CharField(max_length=30,unique=True)
	application_name = models.CharField(max_length=30)
	git_url = models.CharField(max_length=256)
	git_branch = models.CharField(max_length=30)
	platform_version = models.CharField(blank=True, max_length=30)
	cpu =  models.IntegerField(null=True, blank=True)
	memory = models.IntegerField(null=True, blank=True)
	build_tool = models.CharField(blank=True, max_length=30)
	mysql_password = models.CharField( blank=True, max_length=30)
	mongo_password = models.CharField(blank=True, max_length=30)
	env_key1 = models.CharField(blank=True,max_length=30)
	env_value1 = models.CharField(blank=True,max_length=500)
	env_key2 = models.CharField(blank=True,max_length=30)
	env_value2 = models.CharField( blank=True,max_length=500)
	env_key3 = models.CharField( blank=True,max_length=30)
	env_value3 = models.CharField( blank=True,max_length=500)
	env_key4 = models.CharField( blank=True,max_length=30)
	env_value4 = models.CharField( blank=True,max_length=500)
	env_key5 = models.CharField(blank=True,max_length=30)
	env_value5 = models.CharField( blank=True,max_length=500)
	env_key6 = models.CharField(blank=True,max_length=30)
	env_value6 = models.CharField( blank=True,max_length=500)
	env_key7 = models.CharField( blank=True,max_length=30)
	env_value7 = models.CharField( blank=True,max_length=500)
	env_key8 = models.CharField( blank=True,max_length=30)
	env_value8 = models.CharField( blank=True,max_length=500)
	env_key9 = models.CharField( blank=True,max_length=30)
	env_value9 = models.CharField( blank=True,max_length=500)
	env_key10 = models.CharField( blank=True,max_length=30)
	env_value10 = models.CharField( blank=True,max_length=500)
	project_flag = models.BooleanField( blank=True, default=False)
	mysql_status = models.CharField(default='Requested',max_length=256)
	mongo_status = models.CharField(default='Requested',max_length=256)
	jenkins_status = models.CharField(default='Requested',max_length=256)
	pub_date = models.DateTimeField('date published',default=timezone.now)
	def __str__(self):
		return self.project_name


class RequestForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['project_flag','pub_date','mysql_status','mongo_status','jenkins_status',]
        #fields = ['requester', 'project_name', 'application_name' , 'git_url','git_branch','platform_version','cpu' , 'memory','build_tool','mysql_password','mongo_password', 
        #'env_key1','env_value1']






# Create your models here.
