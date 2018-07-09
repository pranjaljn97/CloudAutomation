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
import json


def fmail(request,id,posts,jsonfile):
    destpath = settings.ENVFILE_PATH
    name ="dashboard/hostoutput2.json"
    with open(name, 'r') as f:
        plays = json.load(f)
    
    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.ADMIN_MAIL,request.user.email]
    c = {'uname':posts.requester,
                'projectname':posts.project_name,
                'appname':posts.application_name,
                'hostIp':posts.hostIp, }            
    html_content = render_to_string('dashboard/mail2.html', c)
    text_msg = "Final Status"
    subject = "Your requested Stack status"
    send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                )








    
