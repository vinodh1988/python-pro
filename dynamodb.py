import boto3
import os

boto3.Session(
         region_name='us-east-1',
         aws_access_key_id=os.getenv('ACCESS_KEY'),
         aws_secret_access_key=os.getenv('SECRET_KEY')
)

dynamodb=boto3.resource("dynamodb")

print(dynamodb)