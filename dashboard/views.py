# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from .models import RequestForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .models import HostForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.shortcuts import render
from django.template import Context
from .models import Project, Host
from .models import runningstack
from django.contrib.auth.models import User
from django.template.loader import get_template, render_to_string
from dashboard.makeenv import makeenvfile
from dashboard.makeenv import makeEnvHost
from dashboard.mail import sendmail
from dashboard.mail2 import fmail
from dashboard.buildinfo import buildinfo
from dashboard.mail2 import fmail
from dashboard.boto import add_cname_record
from dashboard.boto import add_host_record
from dashboard.rstackpy import rstack
from dashboard.runplaybook import execplaybook
from dashboard.makehostentry import hostentry
from dashboard.checkStatus import HostCheck
from dashboard.models import status
from dashboard.models import Myform
import datetime
import io
import json


@login_required(login_url='/login/')
def dashboard(request):
#   today = datetime.datetime.now().date()
    return render(request, "dashboard/dashboard.html")

@login_required(login_url='/login/')
def user(request):
#   today = datetime.datetime.now().date()
    return render(request, "dashboard/user.html")

@login_required(login_url='/login/')
def thanks(request):
#   today = datetime.datetime.now().date()
    return render(request, "dashboard/thanks.html")

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def cprovider(request):
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('dashboard/cloud-provider.html')
    else:
        form = HostForm()
        hosts = Host.objects.all()
    return render(request, "dashboard/cloud-provider.html", {'hosts': hosts })


@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def hostadded(request, id):
    makeEnvHost(id)
    hostentry(id)
    currpost = Host.objects.get(id=id)
    name = currpost.hostIdentifier
    ip = currpost.hostIp
    add_host_record(name,ip)
    posts = Host.objects.get(pk=id)
    return render(request, "dashboard/hostdetailform.html", {'posts': posts })
    
    

@login_required(login_url='/login/')
def userdata(request):
    uname = request.user.get_username()
    posts = Project.objects.all().filter(requester='admin')

    return render(request, 'dashboard/post_list.html', {'posts': posts })



@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def forapproval(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = Project.objects.all()
     hostInfo = Host.objects.all()  
     return render(request, "dashboard/forapproval.html", {'posts': posts, 'hostInfo': hostInfo })

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def approved(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = Project.objects.all()
     return render(request, "dashboard/approved.html", {'posts': posts })

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def rstackview(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts2 = Project.objects.all().filter(status='Approved')
     rstack(posts2)
     posts = runningstack.objects.all()
     return render(request, "dashboard/runningstack.html", {'posts': posts })




@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def rejected(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = Project.objects.all()
     return render(request, "dashboard/rejected.html", {'posts': posts })


@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def approvedsuccessfully(request, id):
    
    currpost = Project.objects.get(id=id)
    
    posts = Project.objects.all()
    hostInfo = Host.objects.all()
    try:
        makeenvfile(id)
    except:
        msg = "Error in making Env File"
        return render(request, "dashboard/error.html", {'msg': msg })

    print("hi")
    try:
         execplaybook(id)
    except:
         msg = "Error in executing  Ansible Playbook"
         return render(request, "dashboard/error.html", {'msg': msg })
  
    
    jsonfile = currpost.project_name
    appname = currpost.application_name
    hostip = currpost.hostIp
    try:
         buildinfo(request,id,jsonfile,hostip)
    except:
         msg = "Error in fetching final status"
         return render(request, "dashboard/error.html", {'msg': msg })
  
    try:
         add_cname_record(request,id,jsonfile,appname,hostip)
    
    except:
         msg = "Error in adding A record in AWS Route53"
         return render(request, "dashboard/error.html", {'msg': msg })
    currpost.approvedBy = request.user.email
    currpost.status = 'Approved'
    currpost.save()
   
    fmail(request,id,currpost,jsonfile)

    return render(request, "dashboard/detailform1"+".html", {'posts': posts, 'hostInfo': hostInfo })

@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def rejectedsuccessfully(request, id):
    
    currpost = Project.objects.get(id=id)
    currpost.status = 'Rejected'
    currpost.save()
    posts = Project.objects.get(pk=id)
    posts2 = Project.objects.all()

     #mail functionality
    sendmail(request,id,'reject')
    return render(request, "dashboard/forapproval.html", {'posts': posts2 })


@login_required(login_url='/login/')
def detailform(request,id):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = Project.objects.get(pk=id)
     return render(request, "dashboard/detailform.html", {'posts': posts })

@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
@login_required(login_url='/login/')
def hostdetailform(request,id):
#   today = datetime.datetime.now().date()
     
     posts = Host.objects.get(pk=id)
     return render(request, "dashboard/hostdetailform.html", {'posts': posts })

@login_required(login_url='/login/')
def submitted(request,requester):
#   today = datetime.datetime.now().date()
     uname = request.user.email
     posts = Project.objects.all().filter(requester=requester)
     return render(request, "dashboard/submitted.html", {'posts': posts })



@login_required(login_url='/login/')
def finalmail(request,id):
     uname = request.user.get_username()
     posts = Project.objects.get(pk=id)
     fmail(request,id,posts)
     posts2 = Project.objects.all()
     return render(request, "dashboard/approved.html", {'posts': posts2 })

@login_required(login_url='/login/')
def javaform(request): 
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            #pass
            return HttpResponseRedirect('/dashboard/thanks/')  # does nothing, just trigger the validation
    else:
        form = RequestForm()
    return render(request, 'dashboard/java-home.html', {'form': form})


@login_required(login_url='/login/')
def drupalform(request):
    # hostInfo = Host.objects.values_list('hostIdentifier',flat=True)  
    hostInfo = Host.objects.all()  
    
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            sendmail(request,form,'submit')
         
            return HttpResponseRedirect('/dashboard/')  # does nothing, just trigger the validation
        else:
            print(form.errors)   
    else:
        form = RequestForm()
    return render(request, 'dashboard/drupal-home.html', {'form': form,'hostInfo': hostInfo})
# Create your views here.

@login_required(login_url='/login/')
def nodeform(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            #pass
            return HttpResponseRedirect('/dashboard/')  # does nothing, just trigger the validation
    else:
        form = RequestForm()
    return render(request, 'dashboard/node-home.html', {'form': form})

@login_required(login_url='/login/')
def checkstatus(request, id):
    global mysqlstatus
    global mongostatus
    global sshstatus

    posts = Project.objects.get(pk=id)
    hosts = Host.objects.all()
    hostip = posts.hostIp
    projectname = posts.project_name
    appname = posts.application_name
    destpath = settings.ENVFILE_PATH + projectname + '_' + appname + '/'
    mysqluser = posts.MYSQL_USER_NAME_VALUE
    mysqlpass = posts.MYSQL_PASSWORD_VALUE
    mongouser = posts.MONGO_INITDB_ROOT_USERNAME_VALUE
    mongopass = posts.MONGO_INITDB_ROOT_PASSWORD_VALUE 

    hostcheck = HostCheck()
    # 1 method
    dockerstatus = hostcheck.checkDockerStatus(hostip)
    #2nd method
    urlstatus = hostcheck.checkUrlStatus(projectname,appname)
    print dockerstatus
    print urlstatus
    #3rd method
    with open(destpath + posts.project_name+ '_' + str(posts.id)+'.json') as data_file:
        data_loaded = json.load(data_file)
        mysqlport = data_loaded['mysql']['ports']
        mongoport = data_loaded['mongodb']['ports']
        mysqlstatus = hostcheck.checkMysql(hostip, mysqlport, mysqluser, mysqlpass)
        mongostatus = hostcheck.checkMongo(hostip, mongoport, mongouser, mongopass)
        # mysqlstatus = hostcheck.checkMysql('10.1.203.82', 3306, 'root', 'noida123')
        print mysqlstatus
        print mongostatus
    
   
    for host in hosts:
        if(host.hostIp == hostip):
            sshuser = host.hostUsername
            sshpass = host.hostPassword
            sshstatus = hostcheck.checkSSHStatus(hostip, sshuser, sshpass)
            print sshstatus
            break
    
    checkstackoutput = hostcheck.checkStack(projectname, hostip)
    print checkstackoutput
    varnishstatus = checkstackoutput['varnishstatus']
    redisstatus = checkstackoutput['redisstatus']
    nginxstatus = checkstackoutput['nginxstatus']
    if(varnishstatus == True):
        varnishstatus = 'Connection to Varnish established'
    else:
        varnishstatus = "Can't Connect to Varnish"

    if(redisstatus == True):
        redisstatus = 'Connection to Redis established'
    else:
        redisstatus = "Can't Connect to Redis"

    if(nginxstatus == True):
        nginxstatus = 'Connection to Nginx established'
    else:
        nginxstatus = "Can't Connect to Nginx"
    
    varnishid = checkstackoutput['varnishid']
    redisid =  checkstackoutput['redisid']
    nginxid = checkstackoutput['nginxid']
    mongoid = checkstackoutput['mongoid']
    mysqlid = checkstackoutput['mysqlid']

    
    status.objects.all().delete()
    statusentry = status(projectname=projectname,sshstatus=sshstatus, dockerstatus=dockerstatus, urlstatus=urlstatus, mongostatus=mongostatus, mysqlstatus=mysqlstatus, nginxstatus=nginxstatus, varnishstatus=varnishstatus, redisstatus=redisstatus, mysqlid=mysqlid, mongoid=mongoid, varnishid=varnishid, nginxid=nginxid, redisid=redisid )
    statusentry.save()
    allstatus = status.objects.all()
    return render(request, "dashboard/detailform.html", {'posts': posts, 'allstatus': allstatus })

@login_required(login_url='/login/')
def rerun(request,id):
    print("hi rerrun")
    
    posts = Project.objects.get(pk=id)
    if request.method == 'POST':
        print "int"
        form = Myform(request.POST)
        if form.is_valid():
            newbranch = form.cleaned_data['newbranch']
            print newbranch
            posts.git_branch = newbranch
            posts.save()
            try:
                makeenvfile(id)
            except:
                msg = "Error in making Env File"
                return render(request, "dashboard/error.html", {'msg': msg })
            try:
                execplaybook(id)
            except:
                msg = "Error in executing  Ansible Playbook"
                return render(request, "dashboard/error.html", {'msg': msg })
            jsonfile = posts.project_name
            appname = posts.application_name
            hostip = posts.hostIp
            try:
                buildinfo(request,id,jsonfile,hostip)
            except:
                msg = "Error in fetching final status"
                return render(request, "dashboard/error.html", {'msg': msg })
            return HttpResponseRedirect('/dashboard/detailform' + id + '.html')
    else:
        form = Myform()
    return render(request, "dashboard/rerun.html", {'posts': posts })

    # return render(request, "dashboard/rerun.html", {'posts': posts })





