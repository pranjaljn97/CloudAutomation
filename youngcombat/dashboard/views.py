# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required


from .models import RequestForm

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