import boto3
#2017-03-06T00:00:00Z
client = boto3.client('cloudwatch', region_name='us-east-1')

response = client.get_metric_data(
    MetricDataQueries=[
        { 
            'Namespace': 'metrics.tcc',
            'MetricName': 'responseTime',
            'Dimensions': [
                {
                    'Name': 'target',
                    'Value': 'targetName'
                },
                {
                    'Name': 'interval',
                    'Value': 'interval'
                },
                {
                    'Name': 'requestId',
                    'Value': 'coldstarts',
                },
                {
                    'Name': 'isColdStart',
                    'Value': 'isColdStart'
                }
                ],
                'Period': 60,
                'Stat': 'string',
                'Unit': 'Seconds'|'Microseconds'|'Milliseconds'|'Bytes'|'Kilobytes'|'Megabytes'|'Gigabytes'|'Terabytes'|'Bits'|'Kilobits'|'Megabits'|'Gigabits'|'Terabits'|'Percent'|'Count'|'Bytes/Second'|'Kilobytes/Second'|'Megabytes/Second'|'Gigabytes/Second'|'Terabytes/Second'|'Bits/Second'|'Kilobits/Second'|'Megabits/Second'|'Gigabits/Second'|'Terabits/Second'|'Count/Second'|'None'
            },
            'Expression': 'string',
            'Label': 'string',
            'ReturnData': True|False
        },
    ],
    StartTime=datetime(2015, 1, 1),
    EndTime=datetime(2015, 1, 1),
    NextToken='string',
    ScanBy='TimestampDescending'|'TimestampAscending',
    MaxDatapoints=123




)
