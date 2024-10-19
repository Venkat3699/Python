# list all the S3 buckets and list all the s3 buckets, which are not used for last 7 days and delete that buckets

import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError

def list_all_buckets():
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    # List all S3 buckets
    response = s3_client.list_buckets()
    bucket_list = [bucket['Name'] for bucket in response['Buckets']]
    
    print("All S3 buckets:")
    for bucket in bucket_list:
        print(bucket)
    
    return bucket_list

def list_unused_buckets(bucket_list):
    s3_client = boto3.client('s3')
    unused_buckets = []
    
    # Calculate the date 7 days ago from today
    seven_days_ago = datetime.now() - timedelta(days=7)
    
    for bucket_name in bucket_list:
        try:
            # Get the last modified time of objects in the bucket
            response = s3_client.list_objects_v2(Bucket=bucket_name)
            
            if 'Contents' in response:
                # Check if any objects have been modified in the last 7 days
                recent_objects = any(obj['LastModified'] > seven_days_ago for obj in response['Contents'])
                
                if not recent_objects:
                    unused_buckets.append(bucket_name)
            else:
                # If bucket is empty, consider it as unused
                unused_buckets.append(bucket_name)
        except ClientError as e:
            print(f"Error accessing bucket {bucket_name}: {e}")
    
    if unused_buckets:
        print("\nBuckets not used in the last 7 days:")
        for bucket in unused_buckets:
            print(bucket)
    else:
        print("\nNo unused buckets found in the last 7 days.")
    
    return unused_buckets

def delete_unused_buckets(unused_buckets):
    s3_client = boto3.client('s3')
    
    for bucket_name in unused_buckets:
        try:
            # Empty the bucket before deletion
            response = s3_client.list_objects_v2(Bucket=bucket_name)
            
            if 'Contents' in response:
                # Delete all objects in the bucket
                for obj in response['Contents']:
                    s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Emptied bucket: {bucket_name}")
            
            # Delete the bucket
            s3_client.delete_bucket(Bucket=bucket_name)
            print(f"Deleted bucket: {bucket_name}")
        except ClientError as e:
            print(f"Error deleting bucket {bucket_name}: {e}")

def main():
    # Step 1: List all S3 buckets
    all_buckets = list_all_buckets()
    
    # Step 2: Identify unused buckets in the last 7 days
    unused_buckets = list_unused_buckets(all_buckets)
    
    # Step 3: Delete unused buckets
    if unused_buckets:
        delete_unused_buckets(unused_buckets)

if __name__ == "__main__":
    main()
