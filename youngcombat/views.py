from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import render
import datetime

@login_required(login_url='/login/')
def home(request):
#   today = datetime.datetime.now().date()
    return render(request, "youngcombat/home.html")


#def index(request):
#    template = loader.get_template('youngcombat/base.html')
#    today = datetime.datetime.now().date()
#    context = {
#        'today': today,
#    }
#    
#    return HttpResponse(template.render(context, request))

def error(request):
    template = loader.get_template('youngcombat/error.html')
    today = datetime.datetime.now().date()
    context = {
        'today': today,
    }
    
    return HttpResponse(template.render(context, request))

