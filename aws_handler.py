import boto3
import pandas as pd

def connect_to_s3(aws_access_key_id, aws_secret_access_key, region_name='us-east-1'):
    return boto3.client('s3', 
                        aws_access_key_id=aws_access_key_id, 
                        aws_secret_access_key=aws_secret_access_key, 
                        region_name=region_name)

def get_s3_file(s3_client, bucket_name, file_key):
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    file_content = obj['Body'].read()

    # Detect file type and handle structured/unstructured formats
    if file_key.endswith('.csv'):
        df = pd.read_csv(file_content)
        return df
    elif file_key.endswith('.xlsx'):
        df = pd.read_excel(file_content)
        return df
    elif file_key.endswith('.txt'):
        return file_content.decode('utf-8')
    else:
        raise ValueError("Unsupported file type")
