import boto3
from botocore.exceptions import ClientError

def list_snapshots_in_region(region_name):
    ec2_client = boto3.client('ec2', region_name=region_name)
    
    try:
        # Describe snapshots in the specified region
        snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])  # Change this if you want to include other owners
        return snapshots['Snapshots']
    except ClientError as e:
        print(f"Error fetching snapshots: {e}")
        return []

def delete_snapshots(snapshots):
    ec2_client = boto3.client('ec2')
    
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        try:
            # Delete the snapshot
            ec2_client.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted Snapshot: {snapshot_id}")
        except ClientError as e:
            print(f"Error deleting snapshot {snapshot_id}: {e}")

def main():
    region_name = "ap-south-1"
    
    # Step 1: Get all snapshots in the specified region
    snapshots = list_snapshots_in_region(region_name)
    
    if not snapshots:
        print("No snapshots found in the specified region.")
        return
    
    # Step 2: Delete the snapshots
    print(f"Found {len(snapshots)} snapshots. Deleting...")
    delete_snapshots(snapshots)

if __name__ == "__main__":
    main()
