#! /usr/bin/python3
import yaml
import boto3

myclient = boto3.client('ec2', region_name='us-east-2')

with open('config.yaml', 'r') as yam:
    mydata = yaml.load(yam,Loader=yaml.FullLoader)

myclient.run_instance(**mydata)