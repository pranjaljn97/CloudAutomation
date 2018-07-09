# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
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
from django.contrib.auth.models import User
from django.template.loader import get_template, render_to_string
from dashboard.makeenv import makeenvfile
from dashboard.mail import sendmail
from dashboard.mail2 import fmail
from dashboard.buildinfo import buildinfo
from dashboard.mail2 import fmail
from dashboard.boto import add_cname_record
from dashboard.runplaybook import execplaybook

from dashboard.makehostentry import hostentry



import datetime


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

def hostadded(request, id):
    hostentry(id)
    hosts = Host.objects.all()
    return render(request, "dashboard/cloud-provider.html", {'hosts': hosts })
    

@login_required(login_url='/login/')
def userdata(request):
    uname = request.user.get_username()
    posts = Project.objects.all().filter(requester='admin')

    return render(request, 'dashboard/post_list.html', {'posts': posts })



@login_required(login_url='/login/')
def forapproval(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = Project.objects.all()
     hostInfo = Host.objects.all()  
     return render(request, "dashboard/forapproval.html", {'posts': posts, 'hostInfo': hostInfo })

@login_required(login_url='/login/')
def approved(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = Project.objects.all()
     return render(request, "dashboard/approved.html", {'posts': posts })
@login_required(login_url='/login/')
def rejected(request):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = Project.objects.all()
     return render(request, "dashboard/rejected.html", {'posts': posts })



def approvedsuccessfully(request, id):
    
    currpost = Project.objects.get(id=id)
    currpost.status = 'Approved'
    currpost.save()
    posts = Project.objects.all()
    hostInfo = Host.objects.all()  

    #mail functionality
    subject = "Approval Request"
    message = "Congratulations your stack request has been approved"
    from_email = settings.EMAIL_HOST_USER
    umail = request.user.email 
    to_list = [umail]
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    
    #make env file for ansible

    
    makeenvfile(id)
    execplaybook(id)
    jsonfile = currpost.project_name
    appname = currpost.application_name
    hostip = currpost.hostIp
    buildinfo(request,id,jsonfile,hostip)
    add_cname_record(request,id,jsonfile,appname,hostip)
    fmail(request,id,currpost,jsonfile)
    return render(request, "dashboard/detailform1"+".html", {'posts': posts, 'hostInfo': hostInfo })


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

@login_required(login_url='/login/')
def submitted(request,requester):
#   today = datetime.datetime.now().date()
     uname = request.user.email
     posts = Project.objects.all().filter(requester=requester)
     return render(request, "dashboard/submitted.html", {'posts': posts })

@login_required(login_url='/login/')
def rerun(request,id):
    posts = Project.objects.get(pk=id)
    #execplaybook(id)
    buildinfo(request,id)
    return render(request, "dashboard/detailform"+str(id)+".html", {'posts': posts })

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
        form = RequestForm(request.POST)
        if form.is_valid():

            form.save()
            sendmail(request,form,'submit')

            #form2 = RequestForm2(request.POST)
            #if form2.is_valid():
                #instance = form2.save(commit=False)  
                #instance.user = User.objects.get(id=1)
                #instance.save()
         
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