from dashboard.models import Host
import subprocess
import json
import os
import io
def hostentry(id):
    host = Host.objects.get(pk=id)
    ipAddress = host.hostIp
    username = host.hostUsername
    password = host.hostPassword

    hostinfo = "hostname=" + ipAddress + " user=" + username + " password=" + password
    try:
        subprocess.check_call(['./ansibledir/hostadd.sh', './ansibledir/addHost.yml', hostinfo,'dashboard/hostoutput1.json'])
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
            host.status = 'Added Successfully'
            host.save()
            with io.FileIO("/etc/ansible/hosts", "a+") as file:
                file.write("\n" + ipAddress + " ansible_connection=ssh ansible_user=" + username + " ansible_ssh_pass=" + password + " ansible_sudo_pass=" + password)

            
        else:
            host.status = 'Failed'
            host.save()

    


