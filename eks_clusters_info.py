# Python automation file to find the cluster name, status, version and endpoint in aws eks 
import boto3

eks_cluster = boto3.client('eks', region_name="ap-south-1")

cluster_list = eks_cluster.list_cluster()['clusters']

for cluster in cluster_list:
    response = cluster.describe_cluster(name=cluster)
    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_version = cluster_info['version']
    cluster_endpoint = cluster_info['endpoint']
    print(f"Cluster {cluster} status is {cluster_status}")
    print(f"Cluster endpoint: {cluster_endpoint}")
    print(f"Cluster version: {cluster_version}")
