#!/usr/bin/env python
import os
import subprocess
from dashboard.models import Project
from django.conf import settings


def execplaybook(id):
    destpath = settings.ENVFILE_PATH
    post = Project.objects.get(pk=id)
    project_name = post.project_name
    hostip = post.hostIp
    ansiblePath=os.getcwd()+"/ansibledir"

    jsonfilepath = project_name + "_" + str(post.id) + ".json"
    newpath = '''"''' +  jsonfilepath + '''"'''
    print newpath
    subprocess.check_call(['./ansibledir/runplaybook.sh', './ansibledir/main.yml', destpath + jsonfilepath, 'dashboard/hostoutput2.json'])
