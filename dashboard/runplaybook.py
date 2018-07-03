#!/usr/bin/env python
import os
from subprocess import call
from dashboard.models import Project

def execplaybook(id):
    post = Project.objects.get(pk=id)
    project_name = post.project_name
    jsonfilepath = project_name + '_' + str(id)
    ansiblePath=os.getcwd()+"/ansibledir"
    print ansiblePath
    print "Hello"
    call(["sudo ansible-playbook", "main.yml", "--extra-vars", "@" + jsonfilepath], cwd=ansiblePath)
    print "Bye"
