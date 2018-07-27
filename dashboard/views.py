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
from .models import mysqlForm
from .models import mysqluser
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
from dashboard.mysql import buildMysql
from dashboard.mongo import buildMongo
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
from dashboard.checkhoststatus import HoststatusCheck
from dashboard.models import status
from dashboard.models import hoststatus
from dashboard.deleteProj import deleteProj
from dashboard.models import Ports
from dashboard.models import Myform
from dashboard.models import HostdeployForm
from dashboard.models import mongoform
from dashboard.models import mongorequest
import datetime
import io
import json
import os


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
    # try:
    makeEnvHost(id)
    currpost = Host.objects.get(id=id)
    currpost.status = 'Added Successfully'
    currpost.save()
    # except:
    #     msg = "Error in making Host Env File"
    #     return render(request, "dashboard/error.html", {'msg': msg })

    # hostentry(id)
    # currpost = Host.objects.get(id=id)
    # name = currpost.hostIdentifier
    # ip = currpost.hostIp
    # add_host_record(name,ip)
    posts = Host.objects.get(pk=id)
    return render(request, "dashboard/hostdetailform.html", {'posts': posts })

@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def deployhost(request, id):
    try:
        hostentry(id)
        currpost = Host.objects.get(id=id)
        name = currpost.hostIdentifier
        ip = currpost.hostIp
        add_host_record(name,ip)
       
    except:
        msg = "Error in making Host Env File"
        return render(request, "dashboard/error.html", {'msg': msg })

    posts = Host.objects.get(pk=id)
    return render(request, "dashboard/hostdetailform.html", {'posts': posts })

@login_required(login_url='/login/')
def hostcheckstatus(request, id):
    global mysqlstatus
    global mongostatus
    global sshstatus
    # global nginxstatus

    posts = Host.objects.get(pk=id)

    hostip = posts.hostIp
    sshuser = posts.hostUsername
    sshpass = posts.hostPassword
    sqluser = posts.mysqlUsername
    sqlpass = posts.mysqlPassword

    
    hostcheck = HoststatusCheck()
    # 1 method
    if(posts.hostDocker == 'true'):
        dockerstatus = hostcheck.checkhostDockerStatus(hostip)
        print dockerstatus
    else:
        dockerstatus = 'NA'
    #2nd method
    sshstatus = hostcheck.checkhostSSHStatus(hostip, sshuser, sshpass)
    print sshstatus
    #3rd method
    if(posts.hostMysql == 'true'):
        mysqlstatus = hostcheck.checkhostMysql(hostip,3306,sqluser,sqlpass)
        print mysqlstatus
    else:
        mysqlstatus = 'NA'
    #4th method
    if(posts.hostMongo == 'true'):
        mongostatus = hostcheck.checkhostMongo(hostip,27017)
        print mongostatus
    else:
        mongostatus = 'NA'

    hoststatus.objects.all().delete()
    statusentry = hoststatus(sshstatus=sshstatus, dockerstatus=dockerstatus, mongostatus=mongostatus, mysqlstatus=mysqlstatus)
    statusentry.save()
    allstatus = hoststatus.objects.all()
    return render(request, "dashboard/hostdetailform.html", {'posts': posts, 'allstatus': allstatus })



    



    
    

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
    print "in approved"
    currpost = Project.objects.get(id=id)
    # mysqlu = currpost.MYSQL_USER_NAME_VALUE
    # mysqld = currpost.MYSQL_DATABASE_NAME_VALUE
    # mongou = currpost.MONGO_INITDB_ROOT_USERNAME_VALUE
    # mongod = currpost.MONGO_INITDB_DATABASE_VALUE
    # mysqlu = mysqlu + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # mysqld = mysqld + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # mongou = mongou + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # mongod = mongod + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # currpost.MYSQL_USER_NAME_VALUE = mysqlu
    # currpost.MYSQL_DATABASE_NAME_VALUE = mysqld
    # currpost.MONGO_INITDB_ROOT_USERNAME_VALUE = mongou
    # currpost.MONGO_INITDB_DATABASE_VALUE = mongod
    currpost.save()


    
    posts = Project.objects.all()
    hostInfo = Host.objects.all()
    if request.method == 'POST':
        form = HostdeployForm(request.POST)
        if form.is_valid():
            print "inpost"
            # mysqlu = currpost.MYSQL_USER_NAME_VALUE
            # mysqld = currpost.MYSQL_DATABASE_NAME_VALUE
            # mongou = currpost.MONGO_INITDB_ROOT_USERNAME_VALUE
            # mongod = currpost.MONGO_INITDB_DATABASE_VALUE
            # mysqlu = mysqlu + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
            # mysqld = mysqld + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
            # mongou = mongou + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
            # mongod = mongod + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
            # currpost.MYSQL_USER_NAME_VALUE = mysqlu
            # currpost.MYSQL_DATABASE_NAME_VALUE = mysqld
            # currpost.MONGO_INITDB_ROOT_USERNAME_VALUE = mongou
            # currpost.MONGO_INITDB_DATABASE_VALUE = mongod
            # currpost.save()
            
            ip = form.cleaned_data['hostipdeploy']
            print ip
            currpost.hostIp = ip
            
            status = request.POST.get('legacy')
            print status
            currpost.legacy1 = status

            mysqlip = form.cleaned_data['hostiplegacy']
            if(currpost.legacy1 == 'No'):
                mysqlip = 'NA'
            
            currpost.hostIp_mysql = mysqlip
               
            print mysqlip
            currpost.save()

            #handling mysql and mongo
            if(currpost.hostIp_mysql != 'NA'):
                ip = currpost.hostIp_mysql
                hosts = Host.objects.all().filter(hostIp=ip)
                for post in hosts:
                    user = post.mysqlUsername
                    passwd = post.mysqlPassword
                    sqlflag = post.hostMysql
                    mongoflag = post.hostMongo
                
                uname = currpost.MYSQL_USER_NAME_VALUE
                upwd = currpost.MYSQL_PASSWORD_VALUE
                udb = currpost.MYSQL_DATABASE_NAME_VALUE
                print ip
                print user
                print passwd
                print uname 
                print upwd
                print udb 
                
                if sqlflag == 'true':
                    try:
                        buildMysql(ip,user,passwd,uname,upwd,udb)
                    except:
                        msg = "Unable to make mysql request"
                        return render(request, "dashboard/error.html", {'msg': msg })


                uname = currpost.MONGO_INITDB_ROOT_USERNAME_VALUE
                upwd = currpost.MONGO_INITDB_ROOT_PASSWORD_VALUE
                udb = currpost.MONGO_INITDB_DATABASE_VALUE

                for post in hosts:
                    rootuser = post.mongoUsername
                    rootpass = post.mongoPassword
               
                rootdb = 'admin'

                if mongoflag == 'true':
                    try:
                        buildMongo(rootuser, rootpass, rootdb,uname,upwd,udb,ip)
                    except:
                        msg = "Unable to make mongo request"
                        return render(request, "dashboard/error.html", {'msg': msg })


            
            # try:
            makeenvfile(id)
            # except:
            #      msg = "Error in making Env File"
            #      return render(request, "dashboard/error.html", {'msg': msg })

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

    else:
        print "in else"
        form = HostdeployForm()
    return render(request, "dashboard/approvedetailform.html", {'posts': currpost, 'hostInfo': hostInfo })
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
            

            maxkey  = 0
            maxkey = int(form.cleaned_data['total'])
            tot = 0
            maxkey += 1
            lst = []
            d = {}
            proj = form.cleaned_data['project_name']
            newpath = settings.ENVFILE_PATH + 'documents/' + proj + '/'
            newpath1 = r'./documents/' 
            if not os.path.exists(newpath1):
                os.makedirs(newpath1)
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            try:
                to_unicode = unicode
            except NameError:
                to_unicode = str
            destpath = settings.ENVFILE_PATH + 'documents/' + proj + '/'
            p1 = newpath1 + '/extraenv.json'
            p2 = newpath1 + '/extraenvJson.json'
            with open(p1,'wb') as f:
                    f.close()
            with open(p2,'wb') as f:
                    f.close()
            with open(destpath+'extraenv.json','wb') as f:
                    f.close()
            with open(destpath+'extraenvJson.json','wb') as f:
                    f.close()

            for x in range(1,maxkey):
                y = x
                tot += 1
                name = 'key' + str(x) 
                name2 = 'value' + str(x) 
                print(name)
                print(form.cleaned_data[name])
                a = form.cleaned_data[name]
                b = form.cleaned_data[name2]
                p1 = newpath1 + '/extraenv.json'
                with open(p1,'ab') as f:
                    f.write(a+"="+b+"\n")

                d[a]=b

            lst.append(d)
                        
            final = json.dumps(lst)
            p3 = destpath+'extraenvJson.json'
            with io.open(p3, 'w', encoding='utf8') as outfile:
                str_ = json.dumps(d,
                            indent=4, sort_keys=True,
                            separators=(',', ':'), ensure_ascii=False)
                outfile.write(to_unicode(str_))

            filecurrpath = newpath1 + '/extraenv.json'
            filename = 'extraenv.json'
            print destpath + filename
            os.rename(filecurrpath, destpath + filename)

               

            form.save()
            sendmail(request,form,'submit')
         
            return HttpResponseRedirect('/dashboard/')  # does nothing, just trigger the validation
        else:
            print(form.errors)   
    else:
        form = RequestForm()
    with open('dashboard/version.json') as data_file:
        data_loaded = json.load(data_file)
    return render(request, 'dashboard/drupal-home.html', {'form': form,'hostInfo': hostInfo,'data':data_loaded})
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
def deleteProject(request,id):
    posts = Project.objects.get(pk=id)
    hosts = Host.objects.all()
    hostip = posts.hostIp
    projectname = posts.project_name
    appname = posts.application_name

    deleteproj = deleteProj()
    
    # code to delete nginx config file
    for host in hosts:
        if(host.hostIp == hostip):
            user = host.hostUsername
            passwd = host.hostPassword
            nginxConfigFile = deleteproj.nginxVirtual(hostip,user,passwd,projectname)
            print nginxConfigFile
            break 
    
    #code to remove user
    for host in hosts:
        if(host.hostIp == hostip):
            user = host.hostUsername
            passwd = host.hostPassword
            userDel = deleteproj.userDelete(hostip,user,passwd,projectname)
            print userDel
            break 

    # code to free all project related ports
    instance = Ports.objects.filter(projectname=projectname)
    try:
        for i in instance:
            i.delete()
        portSt = "All ports are free now"
        print portSt
    except:
        portSt = "No such project exist"
        return portSt

    # remove DNS entry from route53
    deleteDNS = deleteproj.deleteDNSEntry(projectname,appname,hostip)
    print deleteDNS

    # delete all running containers
    deleteContainer = deleteproj.deleteContainers(hostip,projectname)
    print deleteContainer

    posts.status = 'Deleted'
    posts.save()
    
    deleteprojectoutput = dict()
    deleteprojectoutput['nginxconfig'] = nginxConfigFile
    deleteprojectoutput['userdel'] = userDel
    deleteprojectoutput['portst'] = portSt
    deleteprojectoutput['deletedns'] = deleteDNS
    deleteprojectoutput['deletecontainer'] = deleteContainer

    return render(request,"dashboard/deleteProject.html", {'deleteprojectoutput' : deleteprojectoutput}) 



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
    print "checking docker status"
    dockerstatus = hostcheck.checkDockerStatus(hostip)
    #2nd method
    urlstatus = hostcheck.checkUrlStatus(projectname,appname)
    print dockerstatus
    print urlstatus
    #3rd method
    # with open(destpath + posts.project_name+ '_' + str(posts.id)+'.json') as data_file:
    #     data_loaded = json.load(data_file)
    #     mysqlport = data_loaded['mysql']['ports']
    #     mongoport = data_loaded['mongodb']['ports']
    #     # mysqlstatus = hostcheck.checkMysql(hostip, mysqlport, mysqluser, mysqlpass)
    #     # mongostatus = hostcheck.checkMongo(hostip, mongoport, mongouser, mongopass)
    #     # mysqlstatus = hostcheck.checkMysql('10.1.203.82', 3306, 'root', 'noida123')
    #     print mysqlstatus
    #     print mongostatus
    
   
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
    mongostatus = checkstackoutput['mongostatus']
    mysqlstatus = checkstackoutput['mysqlstatus']
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

    
    if(mysqlstatus == True):
        mysqlstatus = 'Connection to MySql established'
    else:
        mysqlstatus = "Can't Connect to MySql"
    

    if(mongostatus == True):
        mongostatus = 'Connection to Mongo DB established'
    else:
        mongostatus = "Can't Connect to Mongo DB"
    
    
    varnishid = checkstackoutput['varnishid']
    varnishname = checkstackoutput['varnishname']
    varnishst = checkstackoutput['varnishst']

    redisid =  checkstackoutput['redisid']
    redisname =  checkstackoutput['redisname']
    redisst =  checkstackoutput['redisst']

    nginxid = checkstackoutput['nginxid']
    nginxname = checkstackoutput['nginxname']
    nginxst = checkstackoutput['nginxst']

    mongoid = checkstackoutput['mongoid']
    mongoname = checkstackoutput['mongoname']
    mongost = checkstackoutput['mongost']

    mysqlid = checkstackoutput['mysqlid']
    mysqlname = checkstackoutput['mysqlname']
    mysqlst = checkstackoutput['mysqlst']

    
    status.objects.all().delete()
    statusentry = status(projectname=projectname,sshstatus=sshstatus, dockerstatus=dockerstatus, urlstatus=urlstatus, mongostatus=mongostatus, mysqlstatus=mysqlstatus, nginxstatus=nginxstatus, varnishstatus=varnishstatus, redisstatus=redisstatus, mysqlid=mysqlid, mysqlname=mysqlname, mysqlst=mysqlst, mongoid=mongoid, mongoname=mongoname, mongost=mongost, varnishid=varnishid, varnishname=varnishname, varnishst=varnishst, nginxid=nginxid, nginxname=nginxname, nginxst=nginxst, redisid=redisid,redisname=redisname,redisst=redisst )
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
            maxkey  = 0
            maxkey = int(form.cleaned_data['total'])
            tot = 0
            maxkey += 1
            lst = []
            d = {}
            proj = posts.project_name
            destpath = settings.ENVFILE_PATH + 'documents/' + proj + '/'
            with open(destpath+'extraenv.json','wb') as f:
                    f.flush()
                    f.close()
            for x in range(1,maxkey):
                y = x
                tot += 1
                name = 'key' + str(x) 
                name2 = 'value' + str(x) 
                print(name)
                print(form.cleaned_data[name])
                a = form.cleaned_data[name]
                b = form.cleaned_data[name2]
                #newpath1 = r'./documents/'
		        #if not os.path.exists(newpath1):
                #os.makedirs(newpath1)
                filename = 'extraenv.json'
                p1 = destpath + filename

                with open(p1,'ab') as f:
                    f.write(a+"="+b+"\n")

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
            print(form.errors)  
    else:
        form = Myform()
    proj = posts.project_name
    newpath = settings.ENVFILE_PATH + 'documents/' + proj + '/'
    p1 = newpath + 'extraenvJson.json'
    with open(p1) as data_file:
        jsondata = json.load(data_file)
       
    return render(request, "dashboard/rerun.html", {'posts': posts, 'jsondata': jsondata })


@login_required(login_url='/login/')
def mongoformpage(request):
   
    # hostInfo = Host.objects.values_list('hostIdentifier',flat=True)  
    hostInfo = Host.objects.all()  
    
    if request.method == 'POST':
        print "hi"
        form = mongorequest(request.POST)
        if form.is_valid():
            form.save()
            sendmail(request,form,'mongosubmit')
            return HttpResponseRedirect('/dashboard/')  # does nothing, just trigger the validation
        else:
            print(form.errors)   
    else:
        form = mongorequest()
    return render(request, 'dashboard/mongoForm.html', {'form': form,'hostInfo': hostInfo})




@login_required(login_url='/login/')
def mysqlform(request):
    # hostInfo = Host.objects.values_list('hostIdentifier',flat=True)  
    hostInfo = Host.objects.all() 
    
    if request.method == 'POST':
        print "hi"
        form = mysqlForm(request.POST)
        if form.is_valid():
            # dbname = form.cleaned_data[' MYSQL_DATABASE_NAME_VALUE']
            form.save()

            sendmail(request,form,'mysqlsubmit')
         
            return HttpResponseRedirect('/dashboard/')  # does nothing, just trigger the validation
        else:
            print(form.errors)   
    else:
        form = mysqlForm()
    return render(request, 'dashboard/mysqlhome.html', {'form': form,'hostInfo': hostInfo})


@login_required(login_url='/login/')
def submittedmysql(request,requester):
#   today = datetime.datetime.now().date()
    uname = request.user.email
    posts = mysqluser.objects.all().filter(requester=requester)
    return render(request, "dashboard/submittedmysql.html", {'posts': posts })

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def forapprovalmysql(request):
#   today = datetime.datetime.now().date()
     posts = mysqluser.objects.all()
     hostInfo = Host.objects.all()  
     return render(request, "dashboard/forapprovalmysql.html", {'posts': posts, 'hostInfo': hostInfo })

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def approvedmysql(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = mysqluser.objects.all()
     return render(request, "dashboard/approvedmysql.html", {'posts': posts })

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def rejectedmysql(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = mysqluser.objects.all()
     return render(request, "dashboard/rejectedmysql.html", {'posts': posts })


@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def approvedsuccessfullymysql(request, id):
    
    currpost = mysqluser.objects.get(id=id)
    # dbname = currpost.MYSQL_DATABASE_NAME_VALUE
    # username = currpost.MYSQL_USER_NAME_VALUE
    # dbname = dbname + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # username = username + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # currpost.MYSQL_DATABASE_NAME_VALUE = dbname
    # currpost.MYSQL_USER_NAME_VALUE = username
    # currpost.save()
    ip = currpost.hostIp
    posts = Host.objects.all().filter(hostIp=ip)

    for post in posts:
        user = post.mysqlUsername
        passwd = post.mysqlPassword
    host = currpost.hostIp
    uname = currpost.MYSQL_USER_NAME_VALUE
    
    upwd = currpost.MYSQL_PASSWORD_VALUE
    udb = currpost.MYSQL_DATABASE_NAME_VALUE

    res = buildMysql(host,user,passwd,uname,upwd,udb)

    

    if res == 't':

        currpost.status = 'Approved'
        currpost.save()
        # dbname = currpost.MYSQL_DATABASE_NAME_VALUE
        # username = currpost.MYSQL_USER_NAME_VALUE
        # dbname = dbname + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
        # username = username + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
        # currpost.MYSQL_DATABASE_NAME_VALUE = dbname
        # currpost.MYSQL_USER_NAME_VALUE = username
        # currpost.save()
        posts2 = mysqluser.objects.all()
        sendmail(request,id,'approvedmysql')
    else:
         msg = "Error in approving."
         return render(request, "dashboard/error2.html", {'msg': msg })

    posts2 = mysqluser.objects.all()
    return render(request, "dashboard/forapprovalmysql.html", {'posts': posts2 })

@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def rejectedsuccessfullymysql(request, id):
    
    currpost = mysqluser.objects.get(id=id)
    currpost.status = 'Rejected'
    currpost.save()
    posts = mysqluser.objects.get(pk=id)
    posts2 = mysqluser.objects.all()

     #mail functionality
    sendmail(request,id,'rejectmysql')
    return render(request, "dashboard/forapprovalmysql.html", {'posts': posts2 })

@login_required(login_url='/login/')
def submittedmongo(request,requester):
#   today = datetime.datetime.now().date()
    uname = request.user.email
    posts = mongoform.objects.all().filter(requester=requester)
    return render(request, "dashboard/submittedmongo.html", {'posts': posts })

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def forapprovalmongo(request):
#   today = datetime.datetime.now().date()
     posts = mongoform.objects.all()
     hostInfo = Host.objects.all()  
     return render(request, "dashboard/forapprovalmongo.html", {'posts': posts, 'hostInfo': hostInfo })

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def approvedmongo(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = mongoform.objects.all()
     return render(request, "dashboard/approvedmongo.html", {'posts': posts })

@login_required(login_url='/login/')
@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def rejectedmongo(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = mongoform.objects.all()
     return render(request, "dashboard/rejectedmongo.html", {'posts': posts })


@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def approvedsuccessfullymongo(request, id):
    
    currpost = mongoform.objects.get(id=id)
    # mongodb = currpost.MONGO_INITDB_DATABASE_VALUE
    # mongouser = currpost.MONGO_INITDB_ROOT_USERNAME_VALUE
    # mongodb = mongodb + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # mongouser = mongouser + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # currpost.MONGO_INITDB_DATABASE_VALUE = mongodb
    # currpost.MONGO_INITDB_ROOT_USERNAME_VALUE = mongouser
    # currpost.save()
    ip = currpost.hostip
    posts = Host.objects.all().filter(hostIp=ip)

    # for post in posts:
    #     user = post.mysqlUsername
    #     passwd = post.mysqlPassword
    # host = currpost.hostIp
    uname = currpost.MONGO_INITDB_ROOT_USERNAME_VALUE
    upwd = currpost.MONGO_INITDB_ROOT_PASSWORD_VALUE
    udb = currpost.MONGO_INITDB_DATABASE_VALUE

    rootuser = 'tom'
    rootpass = 'jerry'
    rootdb = 'admin'
    
    # try:
    buildMongo(rootuser, rootpass, rootdb,uname,upwd,udb,ip)
    # except:
    #      msg = "Unable to process your request"
    #      return render(request, "dashboard/error.html", {'msg': msg })
    
    currpost.status = 'Approved'
    currpost.save()

    posts2 = mongoform.objects.all()

     #mail functionality
    sendmail(request,id,'approvedmongo')
    # mongodb = currpost.MONGO_INITDB_DATABASE_VALUE
    # mongouser = currpost.MONGO_INITDB_ROOT_USERNAME_VALUE
    # mongodb = mongodb + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # mongouser = mongouser + str(datetime.datetime.now().time().hour) + '_'  + str(datetime.datetime.now().time().minute)
    # currpost.MONGO_INITDB_DATABASE_VALUE = mongodb
    # currpost.MONGO_INITDB_ROOT_USERNAME_VALUE = mongouser
    # currpost.save()
    return render(request, "dashboard/forapprovalmongo.html", {'posts': posts2 })

@user_passes_test(lambda u: u.has_perm('dashboard.permission_code'))
def rejectedsuccessfullymongo(request, id):
    
    currpost = mongoform.objects.get(id=id)
    currpost.status = 'Rejected'
    currpost.save()
    posts = mongoform.objects.get(pk=id)
    posts2 = mongoform.objects.all()

     #mail functionality
    sendmail(request,id,'rejectmongo')
    return render(request, "dashboard/forapprovalmongo.html", {'posts': posts2 })





