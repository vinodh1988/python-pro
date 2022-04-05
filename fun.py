import boto3
import os

client = boto3.client('s3',
         region_name='ap-south-1',
         aws_access_key_id=os.getenv('ACCESS_KEY'),
         aws_secret_access_key=os.getenv('SECRET_KEY')
)

with open('D:\\aws_lab\\about.html', 'rb') as data:
    client.upload_fileobj(data, 'firstbucket5725', 'about.html')

print(client)
print("file uploaded")