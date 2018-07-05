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

def sendmail(request,form):
    
    #message = "Your form has been submitted \n Please verify your details:" + "Project Name:" + projectname
        from_email = settings.EMAIL_HOST_USER
        to_list = [settings.ADMIN_MAIL,request.user.email]
        c = {'uname': form.cleaned_data.get('requester'),
                'projectname': form.cleaned_data.get('project_name'),
                'appname': form.cleaned_data.get('application_name'),}            
        html_content = render_to_string('dashboard/email.html', c)
        text_msg = "Request Approval"
        send_mail(subject, text_msg, from_email, to_list, fail_silently=False, html_message=html_content
                )