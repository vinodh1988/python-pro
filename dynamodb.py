import boto3
import os

boto3.Session(
         region_name='us-east-1',
         aws_access_key_id=os.getenv('ACCESS_KEY'),
         aws_secret_access_key=os.getenv('SECRET_KEY')
)


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