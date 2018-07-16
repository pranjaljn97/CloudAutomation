import io
import sys
import os
from dashboard.models import Project
from django.conf import settings
from .models import RequestForm
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

def sendmail(request,form,stat):
        if stat == "submit":
    #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
                from_email = 'S2P Team <'+settings.EMAIL_HOST_USER+'>'
                to_list = [settings.ADMIN_MAIL,request.user.email]
                c = {'uname': form.cleaned_data.get('requester'),
                        'projectname': form.cleaned_data.get('project_name'),
                        'appname': form.cleaned_data.get('application_name'),
                        'hostIp': form.cleaned_data.get('hostIp'),
                        'git_url': form.cleaned_data.get('git_url'),
                        'git_token': form.cleaned_data.get('git_token'),
                        'status': form.cleaned_data.get('status'),}            
                html_content = render_to_string('dashboard/mail.html', c)
                subject = "Stack Request Recieved"
                text_msg = "Request Recieved"
                send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                        )

        if stat == "reject":
    #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
		post = Project.objects.get(pk=form)
    		requestermail =  post.requester
                from_email = 'S2P Team <'+settings.EMAIL_HOST_USER+'>'
                to_list = [settings.ADMIN_MAIL,request.user.email, requestermail]
                c = {'uname': post.requester,
                        'projectname': post.project_name ,
                        'appname': post.application_name ,
                        'hostIp': post.hostIp ,
                        'git_url': post.git_url ,
                        'git_token': post.git_token ,}            
                html_content = render_to_string('dashboard/rejectmail.html', c)
                subject = "Stack Request Rejected"
                text_msg = "Request Recieved"
                send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                        )
               
