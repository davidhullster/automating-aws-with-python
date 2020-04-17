# coding: utf-8
import boto3
session = boto3.Session(profile_name='dhull-devopspro-7489630')
session
aws s3 ls
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='dhull-videolyzervideos')
session.region_name
session
bucket = s3.create_bucket(Bucket='dhull-videolyzervideos', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
bucket = s3.create_bucket(Bucket='dhullvideolyzervideos', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
from pathlib import Path
get_ipython().run_line_magic('ls', '/Users/dhull/Downloads/*.mp4')
get_ipython().run_line_magic('ls', '/home/dhull/Downloads/*.mp4')
pathname = '~/Downloads/Pexels Videos 2759442.mp4'
path = Path(pathname).expanduser().resolve()
print(path)
bucket.upload_file(str(path), str(path.name))
rekognition_client = session.client('rekognition')
session = boto3.Session(profile_name='dhull-devopspro-7489630', region_name='us-west-2')
rekognition_client = session.client('rekognition')
rekognition_client
response = rekognition_client.start_label_detection(Video={'S3Object'" {'Bucket': bucket.name, 'Name': path.name}})
response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
response
get_response = rekognition_client.get_label_detection(JobId=response['JobId'])
get_response
response['JobId'].keys()
get_response.keys()
get_response['JobStatus']
get_response['Labels']
len(get_response['Labels'])
