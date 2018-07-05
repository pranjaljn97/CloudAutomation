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

def fmail(request,id,posts):
    with open('dashboard/123.json', 'r') as f:
        plays = json.load(f)
    stat = ''
    for x in plays['plays']:
        #print(x['tasks'][12]['hosts']['127.0.0.1']['result']['stdout_lines'])
        for y in (x['tasks'][12]['hosts']['127.0.0.1']['result']['stdout_lines']):

            stat = stat + "\n" + y
        print(stat)

    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.ADMIN_MAIL,request.user.email]
    c = {'uname':posts.requester,
                'projectname':posts.project_name,
                'appname':posts.application_name,
                'hostIp':posts.hostIp, 
                'status': stat,}            
    html_content = render_to_string('dashboard/finalmail.html', c)
    text_msg = "Final Status"
    subject = "Your requested Stack status"
    send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                )








    
