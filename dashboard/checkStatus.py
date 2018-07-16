#!/usr/bin/python
import paramiko, sys, getpass, requests
from paramiko import client
import docker, MySQLdb
from pymongo import MongoClient


class HostCheck():
    def checkSSHStatus(self,HOST,USER,PASS):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:    
            client.connect(HOST,username=USER,password=PASS)
            print "SSH connection to %s established" %HOST
            client.close()
            print "Logged out of device %s" %HOST
            return "SSH established successfully"
        except:
            return "SSH failed"

    def checkDockerStatus(self,Host):
        try:
            dockerVer = docker.DockerClient(base_url='tcp://'+Host+':2735').version()
            dockerres = str(dockerVer['Components'][0]['Version'])
            return "Docker working:" + dockerres
        except:
            return "Docker not working"

    def checkUrlStatus(self,projectname,appname):
        try:    
            res = requests.get('http://' + projectname+'-'+appname+'@tothenew.tk')
            response =  str(res)
            return "Url is working: " + response
        except:
            return "Url is not working"
            

    def checkMysql(self,mysqlHostname, mysqlPort, mysqlUsername, mysqlPassword):
        try:
            myDB = MySQLdb.connect(host="mysqlHostname", port="mysqlPort", user="mysqlUsername", passwd="mysqlPassword")
            handler = myDB.cursor()
            handler.execute("SELECT VERSION()")
            results = handler.fetchall()
            for items in results:
                return "MySql working fine:" + str(items[0]) 
        except:
            return "Can't connect to mysql"

    def checkMongo(self,mongoHostname, mongoPort, mongoUsername, mongoPassword):
        client = MongoClient("mongodb://" + mongoUsername + ":" + mongoPassword + "@" + mongoHostname + ":" + mongoPort,serverSelectionTimeoutMS=10,connectTimeoutMS=1000 )
        try:
            info = client.server_info()
            mongoRes = str(info['version'])
            return "Mongo working fine:" +  mongoRes
        except:
            return "Can't connect to mongo"
    
    def checkStack(self,Projectname,Host):
    	projectname = Projectname
        host = Host
        nginxphpres=requests.get('http://'+host+':2735/services?filters={"mode":["replicated"],"name":["'+projectname+"_nginx_php"'"]}').json()
        if nginxphpres[0]['Spec']['Mode']['Replicated']['Replicas']==1:
	     print "\n"+nginxphpres[0]['Spec']['Name'] + " is running."
        elif nginxphpres[0]['Spec']['Mode']['Replicated']['Replicas']==0:
	     print "\n"+nginxphpres[0]['Spec']['Name'] + " is not running."
        else:
	     print "Service isn't in replicated mode."

    	mysqlres=requests.get('http://'+host+':2735/services?filters={"mode":["replicated"],"name":["'+projectname+"_mysql"'"]}').json()
    	if mysqlres[0]['Spec']['Mode']['Replicated']['Replicas']==1:
	     print "\n"+mysqlres[0]['Spec']['Name'] + " is running."
        elif mysqlres[0]['Spec']['Mode']['Replicated']['Replicas']==0:
	     print "\n"+mysqlres[0]['Spec']['Name'] + " is not running."
        else:
	     print "Service isn't in replicated mode."

        mongores=requests.get('http://'+host+':2735/services?filters={"mode":["replicated"],"name":["'+projectname+"_mongodb"'"]}').json()
        if mongores[0]['Spec']['Mode']['Replicated']['Replicas']==1:
	     print "\n"+mongores[0]['Spec']['Name'] + " is running."
        elif mongores[0]['Spec']['Mode']['Replicated']['Replicas']==0:
	     print "\n"+mongores[0]['Spec']['Name'] + " is not running."
        else:
	     print "Service isn't in replicated mode."
	
        redisres=requests.get('http://'+host+':2735/services?filters={"mode":["replicated"],"name":["'+projectname+"_redis"'"]}').json()
        if redisres[0]['Spec']['Mode']['Replicated']['Replicas']==1:
	     print "\n"+redisres[0]['Spec']['Name'] + " is running."
        elif redisres[0]['Spec']['Mode']['Replicated']['Replicas']==0:
	     print "\n"+redisres[0]['Spec']['Name'] + " is not running."
        else:
	     print "Service isn't in replicated mode."

        varnishres=requests.get('http://'+host+':2735/services?filters={"mode":["replicated"],"name":["'+projectname+"_varnish"'"]}').json()
        if varnishres[0]['Spec']['Mode']['Replicated']['Replicas']==1:
	     print "\n"+varnishres[0]['Spec']['Name'] + " is running."
        elif varnishres[0]['Spec']['Mode']['Replicated']['Replicas']==0:
	     print "\n"+varnishres[0]['Spec']['Name'] + " is not running."
        else:
	     print "Service isn't in replicated mode."


        nginxphpres=requests.get('http://'+host+':2735/containers/json?all=1&filters={ "name":["'+projectname+"_nginx_php"'"]}').json()
        print "\n"+str(nginxphpres[0]['Id']) + " | " + str(nginxphpres[0]['Names'][0]) + " | " + str(nginxphpres[0]['Status'])

        mysqlres=requests.get('http://'+host+':2735/containers/json?all=1&filters={ "name":["'+projectname+"_mysql"'"]}').json()
        print "\n"+str(mysqlres[0]['Id']) + " | " + str(mysqlres[0]['Names'][0]) + " | " + str(mysqlres[0]['Status'])

        mongores=requests.get('http://'+host+':2735/containers/json?all=1&filters={ "name":["'+projectname+"_mongodb"'"]}').json()
        print "\n"+str(mongores[0]['Id']) + " | " + str(mongores[0]['Names'][0]) + " | " + str(mongores[0]['Status'])

        varnishres=requests.get('http://'+host+':2735/containers/json?all=1&filters={ "name":["'+projectname+"_varnish"'"]}').json()
        print "\n"+(varnishres[0]['Id']) + " | " + str(varnishres[0]['Names'][0]) + " | " + str(varnishres[0]['Status'])

        redisres=requests.get('http://'+host+':2735/containers/json?all=1&filters={ "name":["'+projectname+"_redis"'"]}').json()
        print "\n"+(redisres[0]['Id']) + " | " + str(redisres[0]['Names'][0]) + " | " + str(redisres[0]['Status'])

        
