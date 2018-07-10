#!/usr/bin/env python
import os
import subprocess
from dashboard.models import Project
from django.conf import settings


def execplaybook(id):
    
    post = Project.objects.get(pk=id)
    projectname = post.project_name
    appname = post.application_name
    destpath = settings.ENVFILE_PATH + projectname + '_' + appname + '/'
    hostip = post.hostIp
    ansiblePath=os.getcwd()+"/ansibledir"

    jsonfilepath = projectname + "_" + str(post.id) + ".json"
    newpath = '''"''' +  jsonfilepath + '''"'''
    print newpath
    subprocess.check_call(['./ansibledir/runplaybook.sh', './ansibledir/main.yml', destpath + jsonfilepath, destpath + 'hostoutput2.json'])
