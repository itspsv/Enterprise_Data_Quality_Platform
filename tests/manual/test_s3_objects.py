from edqp.cloud.s3_client import S3Client


def main():

    s3 = S3Client()

    objects = s3.list_objects(
        bucket="edqp",
        prefix="raw/",
    )

    print("\nObjects in raw/\n")

    for obj in objects:
        print(obj)


if __name__ == "__main__":
    main()