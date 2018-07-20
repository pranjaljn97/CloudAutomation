#!/usr/bin/env python
import os
import subprocess
from dashboard.models import Project
from django.conf import settings

from datetime import datetime
import datetime

def execplaybook(id):
    
    post = Project.objects.get(pk=id)
    projectname = post.project_name
    appname = post.application_name
    destpath = settings.ENVFILE_PATH + projectname + '_' + appname + '/'
    hostip = post.hostIp
    ansiblePath=os.getcwd()+"/ansibledir"

    jsonfilepath = projectname + "_" + str(post.id) + "_latest.json"
    newpath = '''"''' +  jsonfilepath + '''"'''
    print newpath
    subprocess.check_call(['./ansibledir/runplaybook.sh', './ansibledir/main.yml', destpath + jsonfilepath, destpath + 'hostoutput_latest.json'])

    a = destpath + 'hostoutput_latest.json'
    b = destpath + 'hostoutput' +'_'+ datetime.datetime.now().strftime("%Y%m%d-%H%M%S") +'_.json'
    with open(a, 'rb') as src, open(b, 'wb') as dst:
     copyfileobj_example(src, dst)
     print("done")

def copyfileobj_example(source, dest, buffer_size=1024*1024):
    """      
    Copy a file from source to dest. source and dest
    must be file-like objects, i.e. any object with a read or
    write method, like for example StringIO.
    """
    while True:
        copy_buffer = source.read(buffer_size)
        if not copy_buffer:
            break
        dest.write(copy_buffer)
