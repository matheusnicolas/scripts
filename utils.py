import boto3
from datetime import datetime

client = boto3.client('logs', region_name='us-east-1')

response = client.filter_log_events(
    logGroupName='lougGroupName',
    logStreamNames=[
        'logStreamNames'
    ],
    filterPattern='METRICS'
    #logStreamNamePrefix='[METRICS]'
)

print(response)