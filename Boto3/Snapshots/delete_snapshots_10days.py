# list of snapshots in ap-south-1 region and if the snapshot is not used more than 10 days, and it is not attached to any volume delete that snapshot

import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError

def list_all_snapshots(region_name="ap-south-1"):
    ec2_client = boto3.client('ec2', region_name=region_name)

    try:
        # List all snapshots owned by the current AWS account in the specified region
        snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])
        return snapshots['Snapshots']
    except ClientError as e:
        print(f"Error fetching snapshots: {e}")
        return []

def find_old_unused_snapshots(snapshots, days=10):
    unused_snapshots = []
    current_time = datetime.now()
    
    # Calculate the threshold date, which is 'days' ago from today
    threshold_date = current_time - timedelta(days=days)

    for snapshot in snapshots:
        # Check if the snapshot is not attached to a volume and is older than 'days' days
        if not snapshot.get('VolumeId'):
            snapshot_date = snapshot['StartTime'].replace(tzinfo=None)  # Remove timezone for comparison
            if snapshot_date < threshold_date:
                unused_snapshots.append(snapshot)
    
    return unused_snapshots

def delete_unused_snapshots(unused_snapshots):
    ec2_client = boto3.client('ec2')
    
    for snapshot in unused_snapshots:
        snapshot_id = snapshot['SnapshotId']
        created_by = snapshot['OwnerId']
        try:
            # Delete the unused snapshot
            ec2_client.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted Snapshot: {snapshot_id}, Created by User (AWS Account ID): {created_by}")
        except ClientError as e:
            print(f"Error deleting snapshot {snapshot_id}: {e}")

def main():
    # Step 1: List all snapshots in ap-south-1 region
    all_snapshots = list_all_snapshots(region_name="ap-south-1")
    
    if not all_snapshots:
        print("No snapshots found.")
        return
    
    # Step 2: Find unused snapshots older than 10 days
    unused_snapshots = find_old_unused_snapshots(all_snapshots, days=10)
    
    if unused_snapshots:
        print(f"Found {len(unused_snapshots)} unused snapshots older than 10 days:")
        for snapshot in unused_snapshots:
            print(f"Snapshot ID: {snapshot['SnapshotId']}, Created by User: {snapshot['OwnerId']}")
        
        # Step 3: Delete unused snapshots
        delete_unused_snapshots(unused_snapshots)
    else:
        print("No unused snapshots older than 10 days found.")

if __name__ == "__main__":
    main()
