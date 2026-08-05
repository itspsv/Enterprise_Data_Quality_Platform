from edqp.cloud.s3_client import S3Client


def main():

    s3 = S3Client()

    buckets = s3.list_buckets()

    print("\nAvailable Buckets\n")

    for bucket in buckets:
        print(bucket)


if __name__ == "__main__":
    main()