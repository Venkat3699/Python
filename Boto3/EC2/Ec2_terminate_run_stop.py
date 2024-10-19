# Terminate the instances, which are running and stopped state
import boto3

def terminate_ec2_instances():
    region_name = "ap-south-1"
    ec2_client = boto3.client("ec2", region_name=region_name)

    # Describe all instances with running and stopped states
    response = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running', 'stopped']
            }
        ]
    )
    
    instances_to_terminate = []
    
    # Collect all instance IDs from the response
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instances_to_terminate.append(instance_id)
    
    if instances_to_terminate:
        print(f"Terminating the following instances: {instances_to_terminate}")
        
        # Terminate the instances
        ec2_client.terminate_instances(InstanceIds=instances_to_terminate)
        
        print("Termination request sent for all running and stopped instances.")
    else:
        print("No running or stopped instances found to terminate.")

terminate_ec2_instances()
