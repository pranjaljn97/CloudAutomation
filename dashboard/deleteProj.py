#!/usr/bin/python
import boto3
import os
import paramiko
import shutil
import time
from paramiko import SSHClient
import docker
import MySQLdb


class deleteProj():

    def deleteDNSEntry(self, projectname, appname, ip):
        client = boto3.client(
            'route53', aws_access_key_id=os.environ['Access_key_ID'], aws_secret_access_key=os.environ['Secret_access_key'])
        try:
            target = ip
            source = projectname + "-" + appname + ".tothenew.tk."
            response = client.change_resource_record_sets(
                HostedZoneId=os.environ['HostedZone'],
                ChangeBatch={
                    'Changes': [
                            {
                                'Action': 'DELETE',
                                'ResourceRecordSet': {
                                    'Name': source,
                                    'Type': 'A',
                                    'TTL': 300,
                                    'ResourceRecords': [{'Value': target}]
                                }
                            }]
                })

            return "Released all DNS entry"
        except:
            return "Error while releasing DNS entry"

    def nginxVirtual(self, HOST, USER, PASS, projectname):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(HOST, username=USER, password=PASS)
            print "SSH connection to %s established" % HOST
            channel = client.invoke_shell()
            channel.send("sudo rm /etc/nginx/sites-enabled/" +
                         projectname+".conf")
            channel.send("\n" + PASS + "\n")
            time.sleep(1)
            output = channel.recv(1024)
            print output
            client.close()
            return "successfully removed nginx virtual config files"
        except:
            client.close()
            return "failed to remove nginx virtual config files"

    def userDelete(self, HOST, USER, PASS, projectname):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(HOST, username=USER, password=PASS)
            print "SSH connection to %s established" % HOST
            channel = client.invoke_shell()
            channel.send("sudo userdel "+projectname)
            channel.send("\n" + PASS + "\n")
            time.sleep(1)
            output = channel.recv(1024)
            print output
            client.close()
            return "successfully removed user"
        except:
            return "Failed to remove user"

    def deleteContainers(self, Host, projectname):
        try:
            cli = docker.APIClient(base_url='tcp://'+Host+':2735')
            cli.remove_service(projectname+'_nginx_php')
            cli.remove_service(projectname+"_mysql")
            cli.remove_service(projectname+"_mongodb")
            cli.remove_service(projectname+"_redis")
            cli.remove_service(projectname+"_varnish")
            return "All services deleted successfully"
        except:
            return "Services are already removed"
