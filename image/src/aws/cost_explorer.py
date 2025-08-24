from datetime import datetime, timedelta
import boto3

client = boto3.client('ce', region_name='sa-east-1')

end = datetime.now()
start = end - timedelta(end.day - 1)

def get_cost():
    return client.get_cost_and_usage(
        TimePeriod={
            'Start': start.strftime('%Y-%m-%d'),
            'End': end.strftime('%Y-%m-%d')
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            },
        ]
    )