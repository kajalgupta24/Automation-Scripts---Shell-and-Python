import boto3
import schedule

ec2_client = boto3.client('ec2', region_name = "ap-south-1")


def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name':'tag:Environment',
                'Value': ['Production']
            }
        ]
    )
    for volume in volumes['volumes']:
        snapshot = ec2_client.create_snapshot(VolumeId=volume['VolumeId'])
        print(snapshot)


schedule.every().day.do(create_volume_snapshots)

while True:
    schedule.run_pending()
