# S3 bucket creation, without public access and Enable Versioning in ap-south-1 region

import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name):
    region_name = "ap-south-1"
    s3_client = boto3.client("s3", region_name=region_name)

    try:
        # Create the S3 bucket
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region_name}
        )
        print(f"Bucket '{bucket_name}' created successfully in {region_name}.")
        
        # Set bucket policy to block public access
        s3_client.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
        print(f"Public access blocked for bucket '{bucket_name}'.")

        # Enable versioning on the bucket
        s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={
                'Status': 'Enabled'
            }
        )
        print(f"Versioning enabled for bucket '{bucket_name}'.")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
create_s3_bucket('demo-yt-2024-10')
