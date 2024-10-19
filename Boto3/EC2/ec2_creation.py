import boto3

def ec2_instance():
    region_name = "ap-south-1"
    ec2_client = boto3.client("ec2", region_name=region_name)
    instances = ec2_client.run_instances(
        ImageId="ami-0dee22c13ea7a9a67",
        MaxCount=1,
        MinCount=1,
        InstanceType="t2.micro",
        KeyName="Ravi_Mumbai"
    )
    instance_id = instances["Instances"][0]["InstanceId"]
    print(f'The instance launched in {region_name}: {instance_id}')

ec2_instance()