import json
import boto3
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('PracticeFormDatabase')
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    
    # Get info from event
    gender = event['gender']
    age = event['age']
    howToKnow = event['howToKnow']
    howOften = event['howOften']
    howContent = event['howContent']
    request = event['request']
    
    # Put the item into the table
    response = table.put_item(
        Item={
         'ID': howToKnow+howOften,
         'Age': age,
         'Gender': gender,
         'HowToKnow': howToKnow,
         'HowOften': howOften,
         'HowContent': howContent,
         'Request': request
        })
        
    return {
        'statusCode': 200,
        'body': json.dumps(gender)
    }
