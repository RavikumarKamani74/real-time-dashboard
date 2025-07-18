import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Metrics')  # ✅ your actual table name

def lambda_handler(event, context):
    try:
        print("Event:", json.dumps(event))  # debug

        # Get the query string parameter safely
        metric_id = event.get('queryStringParameters', {}).get('metric_id', 'cpu')

        # Query the table by partition key
        response = table.query(
            KeyConditionExpression=Key('metric_id').eq(metric_id),
            ScanIndexForward=False,
            Limit=10
        )

        # Convert Decimal to float
        items = response['Items']
        for item in items:
            for k, v in item.items():
                if isinstance(v, Decimal):
                    item[k] = float(v)

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(items)
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
