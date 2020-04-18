# coding: utf-8
import boto3
session = boto3.Session(profile_name='dhull-devopspro-7489630')
as_client = session.client('autoscaling')

as_client.execute_policy(AutoScalingGroupName='NotifonSG', PolicyName='Scale Up')