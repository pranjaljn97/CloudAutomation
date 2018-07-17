from dashboard.models import runningstack
from dashboard.models import Ports
import paramiko, sys, getpass, requests
from dashboard.models import Host, Project
from paramiko import client
import docker
import MySQLdb

def checkMysql(mysqlHostname, mysqlPort, mysqlUsername, mysqlPassword):
    res = 'False'
    try:
        myDB = MySQLdb.connect(host=mysqlHostname, port=mysqlPort, user=mysqlUsername, passwd=mysqlPassword)
        handler = myDB.cursor()
        handler.execute("SELECT VERSION()")
        results = handler.fetchall()
        for items in results:
            print items[0]
        res = 'True'
    except:
        print "Can't connect to mysql"
        res = 'False'
    return res

def checkSSHStatus(hip):
    print("Helloddddddddddddd")
    res = "False"
    try:
        host = Host.objects.all().filter(hostIp=hip)
        for h1 in host:
            HOST = h1.hostIp
            USER = h1.hostUsername
            PASS = h1.hostPassword
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                client.connect(HOST,username=USER,password=PASS)
                print "SSH connection to %s established" %HOST
                client.close()
                print "Logged out of device %s" %HOST
                res = "True"
            except:
                print "failed to ssh to %s" %HOST
                res = "False"
    except:
        res = "False" 
    return res
def checkUrlStatus(url):
    res = 'False'
    try:
        if requests.get(url) == '<Response [200]>':
            res = 'True'
        else:
            res = "False"
    except:
        res = "False" 
    return res    

def rstack(posts):
    for post in posts:
        
        projname = post.project_name
        appname = post.application_name
        obj = runningstack.objects.all().filter(projectname=projname)
        if len(obj) == 0:
            host = runningstack(projectname=projname)
            host.save()
        else:
            print("Already Exist")

    for post in posts:
   
        projname = post.project_name
        appname = post.application_name
        approvedBy = post.approvedBy

        url = projname +'-'+ appname +'.tothenew.tk'
        urlstatus = checkUrlStatus(url)
        hip = post.hostIp
        hstatus = checkSSHStatus(hip)
        mysqluname = post.MYSQL_USER_NAME_VALUE
        mysqlupwd = post.MYSQL_PASSWORD_VALUE
        mongouname = post.MONGO_INITDB_ROOT_USERNAME_VALUE
        mongoupwd = post.MONGO_INITDB_ROOT_PASSWORD_VALUE
        obj = Ports.objects.all().filter(projectname=projname).filter(ptype='nginx')
        for o1 in obj:
                nginxport = o1.port
                obj2 = Ports.objects.all().filter(projectname=projname).filter(ptype='varnish')
                for o2 in obj2:
                    varnishport = o2.port

        currpost = runningstack.objects.get(projectname=projname)

        currpost.status = 'Approved'
        currpost.url = url
        currpost.urlStatus = urlstatus
        currpost.hostIp = post.hostIp
        currpost.hostStatus = hstatus
        currpost.approvedBy = approvedBy
        currpost.nginxport = nginxport
        currpost.varnishport = varnishport
        currpost.mysqluname = mysqluname
        currpost.mysqlupwd = mysqlupwd
        currpost.mysqlstatus = checkMysql(hip,'3306', mysqluname, mysqlupwd)
        currpost.mongouname = mongouname
        currpost.mongoupwd = mongoupwd
        currpost.mongostatus = 'Check Mongo Status'
        currpost.save()
