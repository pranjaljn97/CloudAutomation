# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pymongo
import json
import MySQLdb
import time
from pymongo import MongoClient
#import variables
from django.contrib import admin
from .models import Project
#from jenkinsapi.jenkins import Jenkins
import jenkins


def create_mysql(modeladmin, request, queryset):
    for query in queryset:
    	mysql='mysql'
    	user_name='tarunsaxena'
    	#data=connect_db(query.project_name,query.application_name,mysql,user_name,query.mysql_password)
    	#print data
        #query.env_key4 = data
        #query.mysql_status = data['db_name']+data['db_user']+str(' is created')
        query.mysql_status='Created'
        query.save()
create_mysql.short_description = 'CreateMySQL_Database'

def connect_db(name1,name2,db_type,user_name,password):
	print db_type
	if db_type == 'mongodb':
   		#project=variables.project_name
   		project=str(name1)+str(name2)
   		user=user_name
   		db_name="gc_"+project
   		client_mongo = MongoClient('35.154.197.182:27017')
   		db=client_mongo.db_name
   		client_mongo.db_name.add_user(user, passoword, roles=[{'role':'readWrite','db':db_name}])
              
	if db_type == 'mysql':
               
   		#project=variables.project_name
   		project=str(name1)+str(name2)
   		user=user_name
   		db_name="gc_"+project
   		db=MySQLdb.connect(host="35.154.197.182",user="geekcombat",passwd="igdefault")
   		cur = db.cursor()
   		cur.execute("CREATE DATABASE "+db_name)
   		cur.execute("CREATE USER '"+user+"'@'%' IDENTIFIED BY '"+password+"';")
   		cur.execute("GRANT ALL ON "+db_name+".* TO '"+user+"'@'%'");
   		#cur.execute("flush priviliges;")
	return ({'db_name':db_name,'db_user':user,'db_type':db_type})         
#db="mysql"
#user_name="admin-gc"
#password="igdefault"
#connect_db(db,user_name,password)
def trigger_jenkins(modeladmin, request, queryset):
    for query in queryset:
    	query.jenkins_status='Jenkins Trigger Started'
    	data=build_jenkins(query.project_name,query.application_name,query.git_url,query.git_branch,query.requester)
    	print data
        #query.env_key5 = data
        query.jenkins_status='Jenkins Triggered'
        query.save()
trigger_jenkins.short_description = 'TriggerJenkins'

#from jenkinsapi.jenkins import jenkins
import jenkins
import time

def build_jenkins(PROJECT_NAME,APP_NAME,GIT_REPO_URL,GIT_BRANCH,USERNAME,BUILD_TOOL = 'gradle'):
	jenkins_url = "http://gc-jenkins.tothenew.com"
	username = "anup.yadav@tothenew.com"
	token = "9c7251de24767d33e75768413d8f7fde"
	job = "DSL_JOB_MAYANK"
	#APP_NAME = APP_NAME
	#GIT_REPO_URL = GIT_REPO_URL
	#GIT_BRANCH = GIT_BRANCH
	print GIT_BRANCH
	print GIT_REPO_URL
	ENV = 'qa'
	#BUILD_TOOL = BUILD_TOOL
	jenkins_job_name= PROJECT_NAME+'-'+APP_NAME+'-'+ENV
	con = jenkins.Jenkins(jenkins_url, username=username, password=token)
	print con
	con.build_job(job, {'PROJECT_NAME':PROJECT_NAME,'APP_NAME': APP_NAME,'GIT_REPO_URL': GIT_REPO_URL,'GIT_BRANCH': GIT_BRANCH,'ENV': ENV, 'BUILD_TOOL': BUILD_TOOL,'USERNAME': USERNAME})
	#status = con.get_job(job).is_queued_or_running()
	#print status

	print 'jenkins DSL-JOB job Triggered'
	time.sleep(20)
	print 'sleep end'

	print jenkins_job_name
	print type(jenkins_job_name)
	new_job=str(jenkins_job_name)

	print 'Running '+jenkins_job_name
	con.build_job(new_job, {'ENV':ENV,'APP_NAME': APP_NAME,'BRANCH': GIT_BRANCH, 'USERNAME': USERNAME})
	print con
	return 'Done'

	#running = con.get_job(new_job).is_queued_or_running()
	#print running
	#while running:
	# print running
	# running = jenkin.get_job(created_jenkins_job).is_queued_or_running()
	# latestBuild=jenkin.get_job(created_jenkins_job).get_last_build().get_last_build()
	# print latestBuild.get_status()


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'requester', 'application_name', 'jenkins_status', 'mysql_status','mongo_status']
    actions = [create_mysql,trigger_jenkins, ]

admin.site.register(Project, ProjectAdmin)
