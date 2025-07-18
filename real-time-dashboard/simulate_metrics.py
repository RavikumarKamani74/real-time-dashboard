import boto3
import time
import random
from datetime import datetime
from decimal import Decimal

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='ap-south-2')
table = dynamodb.Table('Metrics')

def generate_cpu_metric():
    return Decimal(str(round(random.uniform(40.0, 100.0), 2)))

while True:
    timestamp = int(time.time())
    value = generate_cpu_metric()

    item = {
        'metric_id': 'cpu',
        'timestamp': Decimal(str(timestamp)),  # Optional: keep consistent
        'value': value
    }

    try:
        table.put_item(Item=item)
        print(f"[{datetime.fromtimestamp(timestamp)}] Inserted CPU metric: {value}%")
    except Exception as e:
        print("❌ Error inserting item:", str(e))

    time.sleep(10)
