from edqp.warehouse.snowflake_client import SnowflakeClient


def main():

    client = SnowflakeClient()

    result = client.execute(
        "SELECT CURRENT_VERSION();"
    )

    print("\nSnowflake Version\n")

    print(result)

    client.close()


if __name__ == "__main__":
    main()