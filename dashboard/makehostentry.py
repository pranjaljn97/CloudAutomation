from dashboard.models import Host
import subprocess
def hostentry(id):
    host = Host.objects.get(pk=id)
    ipAddress = host.hostIp
    username = host.hostUsername
    password = host.hostPassword

    # hostinfo = dict()
    # hostinfo['hostname'] = ipAddress
    # hostinfo['user'] = username
    # hostinfo['password'] = password

    hostinfo = "hostname=" + ipAddress + " user=" + username + " password=" + password
    
    subprocess.check_call(['./ansibledir/hostadd.sh', './ansibledir/addHost.yml', hostinfo])
