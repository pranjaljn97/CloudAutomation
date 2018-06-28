# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required


from .models import RequestForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.shortcuts import render
from .models import Project
from django.contrib.auth.models import User

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
def cloudprovider(request):
    uname = request.user.get_username()
    if uname == 'admin':
#   today = datetime.datetime.now().date()
        return render(request, "dashboard/cloud-provider.html")
    else:
        return render(request, "dashboard/noauth.html")

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
     return render(request, "dashboard/forapproval.html", {'posts': posts })

def forapproval1(request, id):
    
    currpost = Project.objects.get(id=id)
    currpost.status = 'Approved'
    currpost.save()
    posts = Project.objects.all()

    #mail functionality
    subject = "Approval Request"
    message = "Congratulations your stack request has been approved"
    from_email = settings.EMAIL_HOST_USER
    to_list = ["mehtamudit1804@gmail.com"]
    send_mail(subject, message, from_email, to_list, fail_silently=False)

   # posts.status = 'Approved'
    #posts.save()
    return render(request, "dashboard/forapproval.html", {'posts': posts })

def forapproval2(request, id):
    
    currpost = Project.objects.get(id=id)
    currpost.status = 'Rejected'
    currpost.save()
    posts = Project.objects.all()

     #mail functionality
    subject = "Approval Request"
    message = "Sorry your stack request has been rejected"
    from_email = settings.EMAIL_HOST_USER
    to_list = ["mehtamudit1804@gmail.com"]
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    #posts.status = newstatus
    #posts = Project.objects.get(pk=id)
    #posts.status = 'Rejected'
    #posts.save()
    return render(request, "dashboard/forapproval.html", {'posts': posts })










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
# Create your views here.

@login_required(login_url='/login/')
def drupalform(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            #pass
         
            return HttpResponseRedirect('/dashboard/')  # does nothing, just trigger the validation
        else:
            print(form.errors)   
    else:
        form = RequestForm()
    return render(request, 'dashboard/drupal-home.html', {'form': form})
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
# Create your views here.