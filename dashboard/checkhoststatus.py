#!/usr/bin/python
import paramiko, sys, getpass, requests
from paramiko import client
import docker, MySQLdb
from pymongo import MongoClient


class HoststatusCheck():
    def checkhostSSHStatus(self,HOST,USER,PASS):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:    
            client.connect(HOST,username=USER,password=PASS, timeout=10)
            print "SSH connection to %s established" %HOST
            client.close()
            print "Logged out of device %s" %HOST
            return "SSH established successfully"
        except:
            return "SSH failed"
    
    def checkhostDockerStatus(self,Host):
        try:
            dockerVer = docker.DockerClient(base_url='tcp://'+Host+':2735', timeout=10).version()
            dockerres = str(dockerVer['Components'][0]['Version'])
            return "Docker working:" + dockerres
        except:
            return "Docker not working"
    
    def checkhostMysql(self,mysqlHostname, mysqlPort, mysqlUsername, mysqlPassword):
        try:
            myDB = MySQLdb.connect(host=mysqlHostname, port=mysqlPort, user=mysqlUsername, passwd=mysqlPassword)
            handler = myDB.cursor()
            print handler
            handler.execute("SELECT VERSION()")
            results = handler.fetchall()
            for items in results:
                return "MySql working fine:" + str(items[0]) 
        except:
            return "Can't connect to mysql"
    
    def checkhostMongo(self,mongoHostname, mongoPort):
        # client = MongoClient("mongodb://" + mongoUsername + ":" + mongoPassword + "@" + mongoHostname + ":" + mongoPort,serverSelectionTimeoutMS=10,connectTimeoutMS=1000 )
        print 'mongodb://' + mongoHostname + ':' + str(mongoPort)
        client = MongoClient('mongodb://' + mongoHostname + ':' + str(mongoPort),serverSelectionTimeoutMS=10000, connectTimeoutMS=10000)
        print client
        try:
            info = client.server_info()
            mongoRes = str(info['version'])
            return "Mongo working fine:" +  mongoRes
        except:
            return "Can't connect to mongo"

