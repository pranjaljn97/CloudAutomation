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
from django.template import Context
from .models import Project
from django.contrib.auth.models import User
from django.template.loader import get_template, render_to_string


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
   
#   today = datetime.datetime.now().date()
    return render(request, "dashboard/cloud-provider.html")
    

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

def approvedsuccessfully(request, id):
    
    currpost = Project.objects.get(id=id)
    currpost.status = 'Approved'
    currpost.save()
    posts = Project.objects.all()

    #mail functionality
    subject = "Approval Request"
    message = "Congratulations your stack request has been approved"
    from_email = settings.EMAIL_HOST_USER
    umail = request.user.email 
    to_list = [umail]
    send_mail(subject, message, from_email, to_list, fail_silently=False)

   # posts.status = 'Approved'
    #posts.save()
    return render(request, "dashboard/forapproval.html", {'posts': posts })

def rejectedsuccessfully(request, id):
    
    currpost = Project.objects.get(id=id)
    currpost.status = 'Rejected'
    currpost.save()
    posts = Project.objects.all()

     #mail functionality
    subject = "Approval Request"
    message = "Sorry your stack request has been rejected"
    umail = request.user.email 
    from_email = settings.EMAIL_HOST_USER
    to_list = [umail]
    send_mail(subject, message, from_email, to_list, fail_silently=False)

    #posts.status = newstatus
    #posts = Project.objects.get(pk=id)
    #posts.status = 'Rejected'
    #posts.save()
    return render(request, "dashboard/forapproval.html", {'posts': posts })








@login_required(login_url='/login/')
def detailform(request,id):
#   today = datetime.datetime.now().date()
     uname = request.user.get_username()
     posts = Project.objects.get(pk=id)
     return render(request, "dashboard/detailform.html", {'posts': posts })
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
            #mail functionality
            uname = request.user.get_username()
            umail = request.user.email 
            projectname = form.cleaned_data.get('project_name')
            appname = form.cleaned_data.get('application_name')

            #varnish data
            varnishversion = form.cleaned_data.get('varnish_version')
            varnishbackendhost = form.cleaned_data.get('VARNISH_BACKEND_HOST_VALUE')
            varnishbackendport = form.cleaned_data.get('VARNISH_BACKEND_PORT_VALUE')
            varnishsecret = form.cleaned_data.get('VARNISH_SECRET_VALUE')
            varnishport = form.cleaned_data.get('VARNISH_PORT_VALUE')
            subject = "Request Submitted"
            #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
            from_email = settings.EMAIL_HOST_USER
            to_list = [umail]
            c = {'uname': uname,
                        'projectname': projectname,
                        'appname': appname,
                        'varnishversion': varnishversion,
                        'varnishbackendhost': varnishbackendhost,
                        'varnishbackendport': varnishbackendport,
                        'varnishsecret': varnishsecret,
                        'varnishport': varnishport}            
            html_content = render_to_string('dashboard/email.html', c)
            text_msg = "Request Approval"

            send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
            )

         
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