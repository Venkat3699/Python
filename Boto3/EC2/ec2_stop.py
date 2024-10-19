import boto3

def stop_running_instances():
    region_name = "ap-south-1"
    ec2_client = boto3.client("ec2", region_name=region_name)

    # Describe all running instances
    running_instances = ec2_client.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    # Get all the instance IDs of running instances
    instance_ids = []
    for reservation in running_instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    # Stop the running instances
    if instance_ids:
        ec2_client.stop_instances(InstanceIds=instance_ids)
        print(f'Stopped instances: {instance_ids}')
    else:
        print('No running instances found.')

stop_running_instances()
