import boto3
import os
from django.conf import settings

client = boto3.client('route53',aws_access_key_id=[settings.Access_key_ID], aws_secret_access_key=[settings.Secret_access_key])


def add_cname_record(request,id,projectname,appname,ip):
	try:
		target = ip
		source = projectname + "-" + appname + ".tothenew.tk."
		response = client.change_resource_record_sets(
        HostedZoneId=[settings.HostedZone],	
		ChangeBatch= {
						'Comment': 'add %s -> %s' % (source, target),
						'Changes': [
							{
							 'Action': 'UPSERT',
							 'ResourceRecordSet': {
								 'Name': source,
								 'Type': 'A',
								 'TTL': 300,
								 'ResourceRecords': [{'Value': target}]
							}
						}]
		})
	except Exception as e:
                         print("Error in DNS entry")
def add_host_record(name,ip):
	try:
		target = ip
		source = name+ ".tothenew.tk."
		response = client.change_resource_record_sets(
        HostedZoneId=[settings.HostedZone],	
		ChangeBatch= {
						'Comment': 'add %s -> %s' % (source, target),
						'Changes': [
							{
							 'Action': 'UPSERT',
							 'ResourceRecordSet': {
								 'Name': source,
								 'Type': 'A',
								 'TTL': 300,
								 'ResourceRecords': [{'Value': target}]
							}
						}]
		})
	except Exception as e:
                         print("Error in DNS entry")
