import boto3

def upload_file_to_s3(file_path, bucket_name, object_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to S3 bucket {bucket_name} as {object_name}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")