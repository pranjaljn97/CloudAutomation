import boto3
import os

client = boto3.client('route53',aws_access_key_id=os.environ['Access_key_ID'], aws_secret_access_key=os.environ['Secret_access_key'])


def add_cname_record(request,id,name,name2,ip):
	try:
		target = ip
		source = name + "_" + name2 + ".tothenew.tk."
		response = client.change_resource_record_sets(
        HostedZoneId=os.environ['Hosted_Zone'],	
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
                         print e



