#!/usr/bin/env python
import os
import subprocess


from dashboard.models import Project

def execplaybook(id):
    post = Project.objects.get(pk=id)
    project_name = post.project_name
    ansiblePath=os.getcwd()+"/ansibledir"
    jsonfilepath = project_name + "_" + str(post.id) + ".json"
    newpath = '''"''' +  jsonfilepath + '''"'''
    print newpath
    subprocess.check_call(['./ansibledir/runplaybook.sh', './ansibledir/' + jsonfilepath,'./ansibledir/main.yml'])
    
