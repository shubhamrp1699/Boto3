import boto3
import datetime
client_src = boto3.client('ec2')
client = boto3.client('ec2',region_name='ap-south-1')
snapshots = client.describe_snapshots(OwnerIds=['617375357635'])
def get_snapshots_src():
    response = client_src.describe_snapshots(OwnerIds=['617375357635'])
    return response["Snapshots"]

snap = get_snapshots_src()
print(*snap, sep="\n")
for snapshot in snapshots['Snapshots']:
    a= snapshot['StartTime']
    b=a.date()
    c=datetime.datetime.now().date()
    d=c-b
    if d.days==0:
        id = snapshot['SnapshotId']
        client.delete_snapshot(SnapshotId=id)
        print("Deleted Snapshot")
