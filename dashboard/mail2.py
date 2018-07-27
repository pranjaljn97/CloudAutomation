from .models import RequestForm
from .models import Project
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.loader import get_template, render_to_string
import json
from dashboard.models import Ports
from dashboard.models import Host


def fmail(request,id,posts,jsonfile):

    
    post = Project.objects.get(pk=id)

    pname = post.project_name
    obj = Ports.objects.all().filter(projectname=pname).filter(ptype='nginx ssh')
    for o1 in obj:
                print(o1.port)
                nginxport = o1.port
                obj2 = Ports.objects.all().filter(projectname=pname).filter(ptype='varnish ssh')
                for o2 in obj2:
                    varnishport = o2.port
                obj3 = Ports.objects.all().filter(projectname=pname).filter(ptype='mysql ssh')
                for o3 in obj3:
                    mysqlport = o3.port
                obj4 = Ports.objects.all().filter(projectname=pname).filter(ptype='mongo db ssh')
                for o4 in obj4:
                    mongoport = o4.port
                obj5 = Ports.objects.all().filter(projectname=pname).filter(ptype='redis ssh')
                for o5 in obj5:
                    redisport = o5.port

    obj = Ports.objects.all().filter(projectname=pname).filter(ptype='nginx')
    for o1 in obj:
                print(o1.port)
                nginxport1 = o1.port
                obj2 = Ports.objects.all().filter(projectname=pname).filter(ptype='varnish')
                for o2 in obj2:
                    varnishport1 = o2.port
                obj3 = Ports.objects.all().filter(projectname=pname).filter(ptype='mysql')
                for o3 in obj3:
                    mysqlport1 = o3.port
                obj4 = Ports.objects.all().filter(projectname=pname).filter(ptype='mongo db')
                for o4 in obj4:
                    mongoport1 = o4.port
                obj5 = Ports.objects.all().filter(projectname=pname).filter(ptype='redis')
                for o5 in obj5:
                    redisport1 = o5.port

    requestermail =  post.requester
    from_email = 'S2P Team <'+settings.EMAIL_HOST_USER+'>'
    to_list = [settings.ADMIN_MAIL,request.user.email, requestermail]
    hosts = Host.objects.all()
    for host in hosts:
        if host.hostIp == posts.hostIp:
            mysqlflag = host.hostMysql
            mongoflag = host.hostMongo
            break

    legacy = posts.legacy1
    if legacy == 'No':
        c = {'uname':posts.requester,
                    'projectname':posts.project_name,
                    'appname':posts.application_name,
                    'git_url' :posts.git_url,
                    'git_token' :posts.git_token,
                    'hostIp':posts.hostIp,
                    'LegacyHost':posts.hostIp_mysql, 
                    'mysqluname':posts.MYSQL_USER_NAME_VALUE,
                    'mysqlupwd':posts.MYSQL_ROOT_PASSWORD_VALUE,
                    'mongouname':posts.MONGO_INITDB_ROOT_USERNAME_VALUE,
                    'mongoupwd':posts.MONGO_INITDB_ROOT_PASSWORD_VALUE,
                    'nginxport':nginxport,
                    'varnishport':varnishport,
                    'mysqlport':mysqlport,
                    'mongoport':mongoport,
                    'redisport':redisport,
                    'dns':settings.DNS,
                    'nginxport1':nginxport1,
                    'varnishport1':varnishport1,
                    'mysqlport1':mysqlport1,
                    'mongoport1':mongoport1,
                    'redisport1':redisport1,}

        html_content = render_to_string('dashboard/mail2.html', c)
        text_msg = "Final Status"
        subject = "Your requested Stack status"
        send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                    )
    if legacy == 'Yes':
        c = {'uname':posts.requester,
                    'projectname':posts.project_name,
                    'appname':posts.application_name,
                    'git_url' :posts.git_url,
                    'git_token' :posts.git_token,
                    'hostIp':posts.hostIp,
                    'LegacyHost':posts.hostIp_mysql, 
                    'mysqlDb':posts.MYSQL_DATABASE_NAME_VALUE,
                    'mysqluname':posts.MYSQL_USER_NAME_VALUE,
                    'mysqlupwd':posts.MYSQL_PASSWORD_VALUE,
                    'mongoDb':posts.MONGO_INITDB_DATABASE_VALUE,
                    'mongouname':posts.MONGO_INITDB_ROOT_USERNAME_VALUE,
                    'mongoupwd':posts.MONGO_INITDB_ROOT_PASSWORD_VALUE,
                    'nginxport':nginxport,
                    'varnishport':varnishport,
                    'mysqlport':mysqlport,
                    'mongoport':mongoport,
                    'redisport':redisport,
                    'dns':settings.DNS,
                    'mysqlflag':mysqlflag,
                    'mongoflag':mongoflag,
                    'nginxport1':nginxport1,
                    'varnishport1':varnishport1,
                    'mysqlport1':mysqlport1,
                    'mongoport1':mongoport1,
                    'redisport1':redisport1,}               
        html_content = render_to_string('dashboard/mail3.html', c)
        text_msg = "Final Status"
        subject = "Your requested Stack status"
        send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                    )








    
