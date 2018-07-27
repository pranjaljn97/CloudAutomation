import boto3
import os
from django.conf import settings
client = boto3.client('route53',aws_access_key_id=settings.ACCESS_KEY_ID, aws_secret_access_key=settings.SECRET_ACCESS_KEY)


def add_cname_record(request,id,projectname,appname,ip):
	try:
		target = ip
		source = projectname + "-" + appname + settings.DNS
		response = client.change_resource_record_sets(
        HostedZoneId=settings.HOSTEDZONE,	
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
			 print(e)
                         print("Error in DNS entry")
def add_host_record(name,ip):
	try:
		target = ip
		source = name+ settings.DNS
		response = client.change_resource_record_sets(
        HostedZoneId=settings.HOSTEDZONE,	
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
