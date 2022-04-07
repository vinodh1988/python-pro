import boto3
import os

dynamodb=boto3.resource("dynamodb")

table = dynamodb.Table("People")
response = table.put_item(Item={
    "Sno":2,
    "Name":"Praveen",
    "City":"Chennai",
    "State":"TamilNadu"
})

print(response)