# Description
Develop an automation program that takes a YAML configuration file as input and deploys a Linux AWS EC2 instance with two volumes and two users.

Here are some guidelines to follow:

* Create a YAML file based on the configuration provided below for consumption by your application
* You may modify the configuration, but do not do so to the extent that you fundamentally change the exercise
* Include the YAML config file in your repo
* Use Python and Boto3
* Do not use configuration management, provisioning, or IaC tools such as Ansible, CloudFormation, Terraform, etc.

# Requirements
We must be able to:

1. Run your program
2. Deploy the virtual machine
3. SSH into the instance as user1 and user2
4. Read from and write to each of two volumes
5. Please assume the evaluator does not have prior experience executing programs in your chosen language or creating virtual machines via your chosen deployment method. Therefore, please include any documentation necessary to accomplish the above requirements.

# Assumptions going into the assignment.
* The program is meant to take the yaml as input and provision the resources similar to the aformentioned tools (CloudFormation, etc.) hence why they are off limits.
* While the evaluator does not have experience with my chosen language or creating virtual machines, I am working under the assumption they have at least some limited AWS and technical proficency as it isn't explicity stated that they do not. Therefore, I will assume they can login to the AWS Console, create permissions, opening a terminal, generally navigate the AWS platform, and download/navigate to the files. I will not be providing step-by-step instructions for this, but will be including my inputs and requirements.

# Instructions
Make sure that python is installed

Instructions for CentOS:

`yum install -y python3`

Install PyYaml which will allow us to use the yaml file as input with our program:

`pip install awscli boto3 pyyaml`

Run the script:

`python launch.py`

# Documentation
Boto3 Documentation

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

Using Boto3 to launch new EC2 instances
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_instances

