import json
import boto3
# import requests
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('resume_app_state')

    
    response = table.get_item(Key={'id': 'counter'})
    item = response['Item']

    # TODO: overflow ?? when you page has so many visitor..
    count=int(item["value"])
    count=count +1

    table.update_item(
        Key={'id': 'counter'},
        UpdateExpression="set #v = :g",
        ExpressionAttributeValues={
                ':g': str(count)
            },
        ExpressionAttributeNames={
        "#v": "value"
        },
        ReturnValues="UPDATED_NEW"
    )



    return {
        "statusCode": 200,
         "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*",
        },
        "body": json.dumps({
            "count": str(count)
        }),
    }
