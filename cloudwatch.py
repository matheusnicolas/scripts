import boto3
from datetime import datetime
client = boto3.client('cloudwatch', region_name='us-east-1')


response = client.get_metric_data(
   MetricDataQueries=[
        {
            'Id': 'lambda',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'metrics.tcc',
                    'MetricName': 'responseTime',
                    'Dimensions': []
                },
                'Period': 60,
                'Stat': 'Maximum',
                'Unit': 'Milliseconds'
            },
        },
    ],

    StartTime = datetime(2018, 10, 8),
    EndTime = datetime(2018, 10, 9)
)

print(response['MetricDataResults'])