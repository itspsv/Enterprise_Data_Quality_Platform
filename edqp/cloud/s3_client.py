import os

import boto3
from dotenv import load_dotenv


class S3Client:
    """
    Handles Amazon S3 operations.
    """

    def __init__(self):

        load_dotenv()

        self.client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_DEFAULT_REGION"),
        )

    def list_buckets(self):

        response = self.client.list_buckets()

        return [bucket["Name"] for bucket in response["Buckets"]]

    def upload_file(
        self,
        local_file: str,
        bucket: str,
        object_name: str,
    ):

        self.client.upload_file(
            local_file,
            bucket,
            object_name,
        )

        print(f"Uploaded {local_file} -> s3://{bucket}/{object_name}")

    def download_file(
        self,
        bucket: str,
        object_name: str,
        local_file: str,
    ):

        os.makedirs(os.path.dirname(local_file), exist_ok=True)

        self.client.download_file(
            bucket,
            object_name,
            local_file,
        )

        print(f"Downloaded s3://{bucket}/{object_name}")

    def list_objects(
        self,
        bucket: str,
        prefix: str = "",
    ):

        response = self.client.list_objects_v2(
            Bucket=bucket,
            Prefix=prefix,
        )

        if "Contents" not in response:
            return []

        return [obj["Key"] for obj in response["Contents"]]