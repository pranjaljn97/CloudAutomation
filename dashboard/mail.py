import io
import sys
import os
from dashboard.models import Project
from dashboard.models import mysqluser
from dashboard.models import mongoform
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
                        'hostIp': 'NA',
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

        if stat == "mysqlsubmit":
    #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
    		from_email = 'S2P Team <'+settings.EMAIL_HOST_USER+'>'
                to_list = [settings.ADMIN_MAIL,request.user.email]
                c = {'hostip': form.cleaned_data.get('hostIp'),
                        'uname': form.cleaned_data.get('requester'),
                        'dbname': form.cleaned_data.get('MYSQL_DATABASE_NAME_VALUE'),
                        'uname': form.cleaned_data.get('MYSQL_USER_NAME_VALUE'),
                        'upwd': form.cleaned_data.get('MYSQL_PASSWORD_VALUE'),
                        'status': 'Submitted' ,
                        'notification': 'Mysql user creation request Received',
                        'mesg': 'Request Received',}       
                html_content = render_to_string('dashboard/mysqlmail.html', c)
                subject = "Mysql user creation Request Received"
                text_msg = "Request Recieved"
                send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                        )

        if stat == "approvedmysql":
    #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
		post = mysqluser.objects.get(pk=form)
    		requestermail =  post.requester
                from_email = 'S2P Team <'+settings.EMAIL_HOST_USER+'>'
                to_list = [settings.ADMIN_MAIL,request.user.email, requestermail]
                c = {'hostip': post.hostIp,
                        'uname': post.requester,
                        'dbname': post.MYSQL_DATABASE_NAME_VALUE ,
                        'uname': post.MYSQL_USER_NAME_VALUE ,
                        'upwd': post.MYSQL_PASSWORD_VALUE ,
                        'status': post.status ,
                        'notification': 'Congratulations ! Mysql user creation request Approved',
                        'mesg': 'Request Approved',}    
                html_content = render_to_string('dashboard/mysqlmail.html', c)
                subject = "Mysql user creation Request Accepted"
                text_msg = "Request Approved"
                send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                        )


        if stat == "rejectmysql":
    #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
		post = mysqluser.objects.get(pk=form)
    		requestermail =  post.requester
                from_email = 'S2P Team <'+settings.EMAIL_HOST_USER+'>'
                to_list = [settings.ADMIN_MAIL,request.user.email, requestermail]
                c = {'hostip': post.hostIp,
                        'uname': post.requester,
                        'dbname': post.MYSQL_DATABASE_NAME_VALUE ,
                        'uname': post.MYSQL_USER_NAME_VALUE ,
                        'upwd': post.MYSQL_PASSWORD_VALUE ,
                        'status': post.status ,
                        'notification': 'Mysql user creation request Rejected',
                        'mesg': 'Request Rejected',}            
                html_content = render_to_string('dashboard/mysqlmail.html', c)
                subject = "Mysql user creation Request Rejected"
                text_msg = "Request Rejected"
                send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                        )






        if stat == "mongosubmit":
    #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
    		from_email = 'S2P Team <'+settings.EMAIL_HOST_USER+'>'
                to_list = [settings.ADMIN_MAIL,request.user.email]
                c = {'hostip': form.cleaned_data.get('hostip'),
                        'uname': form.cleaned_data.get('requester'),
                        'dbname': form.cleaned_data.get('MONGO_INITDB_DATABASE_VALUE'),
                        'uname': form.cleaned_data.get('MONGO_INITDB_ROOT_USERNAME_VALUE'),
                        'upwd': form.cleaned_data.get('MONGO_INITDB_ROOT_PASSWORD_VALUE'),
                        'status': 'Submitted' ,
                        'notification': 'Your Mongo DB user creation request Received',
                        'mesg': 'Request Received',}       
                html_content = render_to_string('dashboard/mongomail.html', c)
                subject = "Your Mongo DB user creation Request Received"
                text_msg = "Request Recieved"
                send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                        )

        if stat == "approvedmongo":
    #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
		post = mongoform.objects.get(pk=form)
    		requestermail =  post.requester
                from_email = 'S2P Team <'+settings.EMAIL_HOST_USER+'>'
                to_list = [settings.ADMIN_MAIL,request.user.email, requestermail]
                c = {'hostip': post.hostip,
                        'uname': post.requester,
                        'dbname': post.MONGO_INITDB_DATABASE_VALUE,
                        'uname': post.MONGO_INITDB_ROOT_USERNAME_VALUE ,
                        'upwd': post.MONGO_INITDB_ROOT_PASSWORD_VALUE,
                        'status': post.status,
                        'notification': 'Congratulations ! Mongo DB user creation request Approved',
                        'mesg': 'Request Approved',}    
                html_content = render_to_string('dashboard/mongomail.html', c)
                subject = "Mongo DB user creation Request Accepted"
                text_msg = "Request Approved"
                send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                        )


        if stat == "rejectmongo":
    #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
		post = mongoform.objects.get(pk=form)
    		requestermail =  post.requester
                from_email = 'S2P Team <'+settings.EMAIL_HOST_USER+'>'
                to_list = [settings.ADMIN_MAIL,request.user.email, requestermail]
                c = {'hostip': post.hostip,
                        'uname': post.requester,
                        'dbname': post.MONGO_INITDB_DATABASE_VALUE,
                        'uname': post.MONGO_INITDB_ROOT_USERNAME_VALUE,
                        'upwd': post.MONGO_INITDB_ROOT_PASSWORD_VALUE,
                        'status': post.status,
                        'notification': 'Sorry!! Mongo DB user creation request Rejected',
                        'mesg': 'Request Rejected',}            
                html_content = render_to_string('dashboard/mongomail.html', c)
                subject = "Sorry!! Mongo DB user creation Request Rejected"
                text_msg = "Request Rejected"
                send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                        )


               
