import boto3

ec2_client = boto3.client('ec2', region_name='us-west-2')

all_available_vpcs = ec2_client.describe_vpcs()

vpcs = all_available_vpcs['Vpcs']

for vpc in vpcs:
    print(f"The VPC Id - {vpc['VpcId']}")
    cidr_block_assoc_sets = vpc['CidrBlockAssociationSet']
    for cidr_block_assoc_set in cidr_block_assoc_sets:
        print(f"Cidr Block State is - {cidr_block_assoc_set['CidrBlockState']['State']}")
