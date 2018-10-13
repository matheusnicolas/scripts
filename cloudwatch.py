import boto3
from datetime import datetime
import csv

client = boto3.client('cloudwatch', region_name='us-east-1')

with open('metrics_tcc.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        response = client.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'tcc',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': 'metrics.tcc',
                            'MetricName': 'responseTime',
                            "Dimensions": [
                        {
                            "Name": "isColdStart",
                            "Value": row['isColdStart']
                        },
                        {
                            "Name": "requestId",
                            "Value": row['requestId']
                        },
                        {
                            "Name": "interval",
                            "Value": row['interval']
                        },
                        {
                            "Name": "target",
                            "Value": row['target']
                        }
                            ]
                        },
                        'Period': 300,
                        'Stat': 'Maximum',
                        'Unit': 'Milliseconds'
                    },
                        'ReturnData': True
                },
            ],
            StartTime=datetime(2018, 10, 8),
            EndTime=datetime(2018, 10, 10), 
        )   
        print(response['MetricDataResults'])