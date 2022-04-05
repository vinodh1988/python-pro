import boto3
import os

client = boto3.client('s3',
         region_name='ap-south-1',
         aws_access_key_id=os.getenv('ACCESS_KEY'),
         aws_secret_access_key=os.getenv('SECRET_KEY')
)

with open('C:\\Users\\vinodh\\Desktop\\mysql-connector-java-8.0.11.jar', 'rb') as data:
# Upload the file ATA.txt within the Myfolder on S3
    client.upload_fileobj(data, 'firstbucket5725', 'mysql-connector-java-8.0.11.jar')

BUCKET_NAME = 'my_s3_bucket'
BUCKET_FILE_NAME = 'my_file.json'
LOCAL_FILE_NAME = 'downloaded.json'

def download_s3_file():
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)

print(client)

