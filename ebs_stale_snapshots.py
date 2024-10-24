import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get all EBS snapshots
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # Get all the EC2 Instances in running state
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Value': ['running']}])
    active_instance_ids = set()

    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])
    

    for snapshots in response['Snapshots']:
        snapshot_id = snapshots['SnapshotId']
        volume_id = snapshots.get("VolumeId")

        if not volume_id:
            ec2.delete_snapshot(SnapshotId=snapshot_id)

            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volumes.")

        else:

            try:
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])
                if not volume_response['Volumes'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")

            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                   ec2.delete_snapshot('SnapshotId=snapshot_id')
                   print(f"Deleted EBS snapshot {snapshot_id} as its associated voulne was not found.")
