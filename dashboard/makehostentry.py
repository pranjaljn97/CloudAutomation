from dashboard.models import Host
from django.conf import settings
import subprocess
import json
import os
import io
def hostentry(id):
    host = Host.objects.get(pk=id)
    ipAddress = host.hostIp
    hostId = host.hostIdentifier
    hostIp2 = host.hostIp
    username = host.hostUsername
    password = host.hostPassword

    destpath = settings.ENVFILE_PATH + host.hostIdentifier + '_' + host.hostIp + '/'
    filepath = host.hostIdentifier+ '_' + str(host.id)+'.json'
    print(destpath)
    print(filepath)
    try:
        subprocess.check_call(['./ansibledir/hostadd.sh', './ansibledir/addHost.yml', destpath + filepath,'dashboard/hostoutput1.json'])
    except subprocess.CalledProcessError as Error:
        print("Error : %s"% (Error))
    print "hello"
    if(os.stat("dashboard/hostoutput1.json").st_size == 0):
        print("Empty")
        host.status = 'Failed'
        host.save()
    else:
        with open('dashboard/hostoutput1.json', 'r') as f:
            allentries = json.load(f)
        stats = allentries['stats']
        okstatus = stats[ipAddress]['ok']
        failurestatus = stats[ipAddress]['failures']
        if(okstatus != 0 and failurestatus == 0):
            host.status = 'Deployed Successfully'
            host.save()
            with io.FileIO("/etc/ansible/hosts", "a+") as file:
                file.write("\n" + ipAddress + " ansible_connection=ssh ansible_user=" + username + " ansible_ssh_pass=" + password + " ansible_sudo_pass=" + password)

            
        else:
            host.status = 'Failed'
            host.save()

    


