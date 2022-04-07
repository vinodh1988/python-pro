import boto3
import os

dynamodb=boto3.resource("dynamodb")
table = dynamodb.Table("People")
response = table.get_item(
    Key ={
        "Sno": 1
    }
)

print(response['Item'])