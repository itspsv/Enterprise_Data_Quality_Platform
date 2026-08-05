from edqp.cloud.s3_client import S3Client


def main():

    s3 = S3Client()

    s3.upload_file(
        local_file="datasets/raw/customers.csv",
        bucket="edqp",
        object_name="raw/customers.csv",
    )


if __name__ == "__main__":
    main()