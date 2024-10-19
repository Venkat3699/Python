import boto3
from datetime import datetime, timedelta
from botocore.exceptions import ClientError

def list_all_snapshots():
    ec2_client = boto3.client('ec2')
    
    # Get all snapshots owned by the user
    response = ec2_client.describe_snapshots(OwnerIds=['self'])
    
    snapshot_list = []
    for snapshot in response['Snapshots']:
        snapshot_info = {
            'SnapshotId': snapshot['SnapshotId'],
            'StartTime': snapshot['StartTime'],
            'Description': snapshot.get('Description', 'N/A'),
            'OwnerId': snapshot['OwnerId'],
            'Tags': snapshot.get('Tags', [])
        }
        snapshot_list.append(snapshot_info)
    
    return snapshot_list

def check_snapshot_usage(snapshot_list):
    ec2_client = boto3.client('ec2')
    unused_snapshots = []

    # Get current date to calculate the age of snapshots
    current_date = datetime.now()
    
    for snapshot in snapshot_list:
        snapshot_id = snapshot['SnapshotId']
        start_time = snapshot['StartTime']
        
        # Check if the snapshot is attached to any volume
        response = ec2_client.describe_volumes(Filters=[{'Name': 'snapshot-id', 'Values': [snapshot_id]}])
        
        if not response['Volumes']:
            # Snapshot is not attached to any volume
            days_unused = (current_date - start_time.replace(tzinfo=None)).days
            owner_tag = next((tag['Value'] for tag in snapshot['Tags'] if tag['Key'] == 'CreatedBy'), 'Unknown')

            snapshot_info = {
                'SnapshotId': snapshot_id,
                'Owner': owner_tag,
                'DaysUnused': days_unused
            }
            unused_snapshots.append(snapshot_info)
    
    return unused_snapshots

def send_notification(unused_snapshots):
    sns_client = boto3.client('sns')
    # Assume that there is an SNS topic to notify the users
    topic_arn = 'arn:aws:sns:ap-south-1:123456789012:NotifySnapshotOwner'
    
    for snapshot in unused_snapshots:
        snapshot_id = snapshot['SnapshotId']
        owner = snapshot['Owner']
        days_unused = snapshot['DaysUnused']
        
        message = (
            f"Snapshot {snapshot_id} has not been used for {days_unused} days. "
            f"Snapshot Owner: {owner}."
        )
        
        try:
            # Publish the message to the SNS topic
            sns_client.publish(
                TopicArn=topic_arn,
                Message=message,
                Subject=f"Unused Snapshot Alert for {snapshot_id}"
            )
            print(f"Notification sent for snapshot {snapshot_id}.")
        except ClientError as e:
            print(f"Error sending notification for snapshot {snapshot_id}: {e}")

def main():
    # Step 1: List all snapshots
    snapshot_list = list_all_snapshots()
    
    # Step 2: Check if snapshots are unused
    unused_snapshots = check_snapshot_usage(snapshot_list)
    
    if unused_snapshots:
        # Step 3: Send notifications for unused snapshots
        send_notification(unused_snapshots)
    else:
        print("No unused snapshots found.")

if __name__ == "__main__":
    main()
