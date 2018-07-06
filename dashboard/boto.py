import boto3

client = boto3.client('route53')


def add_cname_record(source, target):
	try:
		response = client.change_resource_record_sets(
        HostedZoneId='Z2H4GS4DFI9BRZ',
		ChangeBatch= {
						'Comment': 'add %s -> %s' % (source, target),
						'Changes': [
							{
							 'Action': 'UPSERT',
							 'ResourceRecordSet': {
								 'Name': source,
								 'Type': 'CNAME',
								 'TTL': 300,
								 'ResourceRecords': [{'Value': target}]
							}
						}]
		})
	except Exception as e:
                         print e


add_cname_record('sss.ssp.org.','172.230.201.0')
