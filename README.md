# Description
Develop an automation program that takes a YAML configuration file as input and deploys a Linux AWS EC2 instance with two volumes and two users.

Here are some guidelines to follow:

Create a YAML file based on the configuration provided below for consumption by your application
You may modify the configuration, but do not do so to the extent that you fundamentally change the exercise
Include the YAML config file in your repo
Use Python and Boto3
Do not use configuration management, provisioning, or IaC tools such as Ansible, CloudFormation, Terraform, etc.

# Requirements
We must be able to:

Run your program
Deploy the virtual machine
SSH into the instance as user1 and user2
Read from and write to each of two volumes
Please assume the evaluator does not have prior experience executing programs in your chosen language or creating virtual machines via your chosen deployment method. Therefore, please include any documentation necessary to accomplish the above requirements.
