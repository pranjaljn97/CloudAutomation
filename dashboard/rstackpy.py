from dashboard.models import runningstack
from dashboard.models import Ports
import paramiko, sys, getpass, requests
from dashboard.models import Host, Project
from paramiko import client
import docker
import MySQLdb


def rstack(posts):
    for post in posts:
        
        projname = post.project_name
        appname = post.application_name
        obj = runningstack.objects.all().filter(projectname=projname)
        if len(obj) == 0:
            host = runningstack(projectname=projname)
            host.save()
        else:
            print("Already Exist")

    for post in posts:
   
        projname = post.project_name
        appname = post.application_name
        approvedBy = post.approvedBy

        url = projname +'-'+ appname +'.tothenew.tk'
       
        hip = post.hostIp
      
        mysqluname = post.MYSQL_USER_NAME_VALUE
        mysqlupwd = post.MYSQL_PASSWORD_VALUE
        mongouname = post.MONGO_INITDB_ROOT_USERNAME_VALUE
        mongoupwd = post.MONGO_INITDB_ROOT_PASSWORD_VALUE
        obj = Ports.objects.all().filter(projectname=projname).filter(ptype='nginx')
        for o1 in obj:
                nginxport = o1.port
                obj2 = Ports.objects.all().filter(projectname=projname).filter(ptype='varnish')
                for o2 in obj2:
                    varnishport = o2.port

        currpost = runningstack.objects.get(projectname=projname)

        currpost.status = 'Approved'
        currpost.url = url      
        currpost.hostIp = post.hostIp   
        currpost.approvedBy = approvedBy
        currpost.nginxport = nginxport
        currpost.varnishport = varnishport
        currpost.mysqluname = mysqluname
        currpost.mysqlupwd = mysqlupwd
        currpost.mongouname = mongouname
        currpost.mongoupwd = mongoupwd
        currpost.save()
