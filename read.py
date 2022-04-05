import boto3
import os

client = boto3.client('s3',
         region_name='ap-south-1',
         aws_access_key_id=os.getenv('ACCESS_KEY'),
         aws_secret_access_key=os.getenv('SECRET_KEY')
)

BUCKET_NAME = 'firstbucket5725'
BUCKET_FILE_NAME ='style.css'
LOCAL_FILE_NAME = 'style.css'

client.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)


print(client)
print("Downloaded")

