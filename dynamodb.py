import boto3
import os

dynamodb=boto3.resource("dynamodb")
dynamodb.create_table(
    TableName='People',
    KeySchema=[
      
        {
            "AttributeName": "Sno",
            'KeyType':"HASH"
        }
    ],
    AttributeDefinitions=[
        {
            "AttributeName":"Sno",
            "AttributeType":"N"
        }],
        ProvisionedThroughput={
            'ReadCapacityUnits' :1,
            'WriteCapacityUnits': 1
        }
    
)

print("Table created")

print(dynamodb)