import boto3

ec2_instances_india = boto3.client('ec2', region_name = "ap-south-1")
ec2_resource_india = boto3.resource('ec2', region_name = "ap-south-1")

ec2_instances_paris = boto3.client('ec2', region_name = "eu-west-3")
ec2_resource_paris = boto3.resource('ec2', region_name = "eu-west-3")

ec2_instances_id_india = []
ec2_instances_id_paris = []

reservations_india = ec2_instances_india.describe_instances()['Reservations']

for res in reservations_india:
    instance = res['Instances']
    for ins in instance:
        ec2_instances_id_india.append(ins['InstanceId'])

response = ec2_resource_india.create_tags(
    Resources = ec2_instances_id_india,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'production'
        },
    ]
)


reservations_paris = ec2_instances_paris.describe_instances()['Reservations']

for res in reservations_paris:
    instance_paris = res['Instances']
    for ins in instance_paris:
        ec2_instances_id_paris.append(ins['InstanceId'])

responses = ec2_resource_paris.create_tags(
    Resources = ec2_instances_id_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'development'
        },
    ]
)
