#!/usr/bin/env python
import os
import subprocess
from ansible_subprocess import run_playbook, run_ping

from dashboard.models import Project

def execplaybook(id):
    post = Project.objects.get(pk=id)
    project_name = post.project_name
    ansiblePath=os.getcwd()+"/ansibledir"
<<<<<<< HEAD
    jsonfilepath = project_name + "_" + str(post.id) + ".json"
    newpath = '''"''' +  jsonfilepath + '''"'''
    print newpath
    subprocess.check_call(['./ansibledir/runplaybook.sh', './ansibledir/' + jsonfilepath,'./ansibledir/main.yml'])
    
=======
    print ansiblePath
    print "Hello"
    call(["sudo ansible-playbook", "main.yml", "--extra-vars", "@" + jsonfilepath], cwd=ansiblePath)
    print "Bye"
>>>>>>> 0dd6757383ac49cbab2fa25dc729c104b33a0e27
