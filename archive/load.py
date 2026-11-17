import os 
import json
import logging
from dotenv import load_dotenv
import boto3                #imports the aws package we installed 

#------------------------------------------------------------------------

load_dotenv()               # this beginning gives the python script access to these credientials in our .env file

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME =os.getenv('AWS_BUCKET_NAME')


data_dir = 'data'
file_location = os.listdir(data_dir)


# this below allows us to connect to specific bucket, telling it that we want to connect to an s3 bucket and these are the credientials 

s3_client = boto3.client(
    's3', 
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
)

for file in file_location: 
    to_upload = f'{data_dir}/{file}'  #what we are calling the files we have saved locally to upload in AWS 
    try:                                          
        s3_client.upload_file(to_upload, AWS_BUCKET_NAME, file)  #find file locally, bucket  you want it in, what you want the file to be called in AWS
        print(f'File {file} has successfully uploaded!')
        os.remove(to_upload)
    except Exception as e:
        print(f'Something went wrong. Error: {e}')




