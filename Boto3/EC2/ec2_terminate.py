import boto3

def terminate_stopped_instances():
    region_name = "ap-south-1"
    ec2_client = boto3.client("ec2", region_name=region_name)

    # Describe all running instances
    running_instances = ec2_client.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
    )
    
    # Get all the instance IDs of Stopped instances
    instance_ids = []
    for reservation in running_instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    # Terminate the Stopped instances
    if instance_ids:
        ec2_client.terminate_instances(InstanceIds=instance_ids)
        print(f'Terminated instances: {instance_ids}')
    else:
        print('No stopped instances found.')

terminate_stopped_instances()
