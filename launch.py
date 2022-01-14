#! /usr/bin/python3
import yaml
import boto3


#cidr range for devices needing ssh
cidr_range = '192.168.0.0/20'

with open('config.yaml', 'r') as yam:

    conf = yaml.safe_load(yam)

    ec2 = boto3.resource('ec2')
    conf = conf['server']
    #ideally I would use a for loop as opposed to creating separte variables
    volume1 = conf['volumes'][0]
    user1 = conf['users'][0]
    region = conf['region']


    # create a new EC2 instance
    instances = ec2.create_instances(
        Placement={'AvailabilityZone': region['region']},
        InstanceType=conf['instance_type'],
        MinCount=conf['min_count'],
        MaxCount=conf['max_count'],
        BlockDeviceMappings=[
            {
                'DeviceName': volume1['device'],
                'Ebs': {
                    'VolumeSize': volume1['size_gb']
                }
            }
        ]
    )
