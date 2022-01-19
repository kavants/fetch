#! /usr/bin/python3
import yaml
import boto3
import subprocess;


key_name_pair = 'fetch-keypair'

#cidr range for devices needing ssh
cidr_range = '192.168.0.0/20'

with open('config.yaml', 'r') as yam:

    conf = yaml.safe_load(yam)

    ec2 = boto3.resource('ec2')
    conf = conf['server']
    volume1 = conf['volumes'][0]
    volume2 = conf['volumes'][1]
    user1 = conf['users'][0]
    user2 = conf['users'][1]
    region = conf['region']


#need to utilize bash to mount drives and add users into servers

    insert_bash = '#!/bin/bash\n'
    #volume1 is mounted at launch
    # mount volume2
    create_volume_bash_file = insert_bash + "touch volume.sh"
    echo = insert_bash + "echo " + insert_bash + "\"sudo mkfs.%s %s\n (volume2[\'type\'], volume2[\'device\']) sudo mkdir %s\n (volume2[\'mount\'])\n sudo mount -o rw %s %s\n (volume2[\'device\'], volume2[\'mount\'])\" > volume.sh"       
    volume_create = subprocess.call("./volume.sh")
    # create user1
    create_user1_bash_file = insert_bash + "touch user1.sh"
    echo_user1 =  insert_bash + "echo " + insert_bash + "sudo adduser %s\n  (user1[\'login\']\n sudo mkdir /home/%s/.ssh\n  (user1[\'login\'])\n sudo touch /home/%s/.ssh/authorized_keys\n % (user1[\'login\'])\n sudo echo %s > /home/%s/.ssh/authorized_keys\n' % (user1[\'ssh_key\'], user1[\'login\']))\" > user1.sh"
    user1_create = subprocess.call("./user1.sh") 
    # create user2
    create_user2_bash_file = insert_bash + "touch user2.sh"
    echo_user2 =  insert_bash + "echo " + insert_bash + "sudo adduser %s\n  (user2[\'login\']\n sudo mkdir /home/%s/.ssh\n  (user2[\'login\'])\n sudo touch /home/%s/.ssh/authorized_keys\n % (user2[\'login\'])\n sudo echo %s > /home/%s/.ssh/authorized_keys\n' % (user2[\'ssh_key\'], user1[\'login\']))\" > user2.sh"
    user2_create = subprocess.call("./user2.sh")


    # create a new EC2 instance
    instances = ec2.create_instances(
        Placement={'AvailabilityZone': region['region']},
        InstanceType=conf['instance_type'],
        MinCount=conf['min_count'],
        MaxCount=conf['max_count'],
        UserData=insert_bash,
        BlockDeviceMappings=[
            {
                'DeviceName': volume1['device'],
                'Ebs': {
                    'VolumeSize': volume1['size_gb']
                }
            },
            {
                'DeviceName': volume2['device'],
                'Ebs': {
                    'VolumeSize': volume2['size_gb']
                }
            }
        ]
    )
   
    print('Instance launched successfully')

