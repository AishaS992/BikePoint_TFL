import os
import logging
import boto3


logger = logging.getLogger(__name__)



def load_to_s3(AWS_BUCKET_NAME: str, AWS_ACCESS_KEY: str, AWS_SECRET_ACCESS_KEY: str, data_dir: str):
    """Function to load data into AWS S3 bucket

    Args:
        aws_bucket_name (str): name of AWS S3 bucket
        aws_access_key_id (str): key value (get value from .env in main)
        aws_secret_access_key (str): Secret Value (get value from.env in main)
        data_dir (str): file path to save data to
    """

    s3_client = boto3.client(
    's3', 
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    fileS = os.listdir(data_dir)

    for file in fileS: 
        to_upload = f'{data_dir}/{file}'  #what we are calling the files we have saved locally to upload in AWS 
        try:                                          
            s3_client.upload_file(to_upload, AWS_BUCKET_NAME, file)  #find file locally, bucket  you want it in, what you want the file to be called in AWS
            print(f'File {file} has successfully uploaded!')
            os.remove(to_upload)
        except Exception as e:
            print(f'Something went wrong. Error: {e}')