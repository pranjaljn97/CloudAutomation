#!/usr/bin/python
import paramiko, sys, getpass, requests
# from dashboard.models import Host, Project
from paramiko import client
import docker, MySQLdb
from pymongo import MongoClient
from django.conf import settings


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
        except Exception as e:
            return "SSH failed"

    def checkDockerStatus(self,Host):
        try:
            dockerVer = docker.DockerClient(base_url='tcp://'+Host+':2735').version()
            dockerres = str(dockerVer['Components'][0]['Version'])
            return "Docker working:" + dockerres
        except:
            return "Docker not working"

    def checkUrlStatus(self,projectname,appname):
        # proj = Project.objects.get(pk=id)
        # projectname = proj.project_name
        # appname = proj.application_name
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
            return "Cant connect to mongo"
    
    # def checkContainer(jsonfile):
    #     name = settings.ENVFILE_PATH + projectname + '_' + appname + '/hostoutput2.json'
    #     with open(name, 'r') as f:
    #         jsoninfo = json.load(f)

