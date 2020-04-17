# coding: utf-8
import boto3

session = boto3.Session(profile_name='dhull-devopspro-7489630', region_name='us-west-2')
rekognition_client = session.client('rekognition')

response = rekognition_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
get_response = rekognition_client.get_label_detection(JobId=response['JobId'])
get_response['Labels']
len(get_response['Labels'])
