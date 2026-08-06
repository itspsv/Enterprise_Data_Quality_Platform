import os

import snowflake.connector
from dotenv import load_dotenv


class SnowflakeClient:
    """
    Handles all Snowflake interactions.
    """

    def __init__(self):

        load_dotenv()

        self.connection = snowflake.connector.connect(
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
            database=os.getenv("SNOWFLAKE_DATABASE"),
            schema=os.getenv("SNOWFLAKE_SCHEMA"),
            role=os.getenv("SNOWFLAKE_ROLE"),
        )

    def execute(self, sql: str):

        cursor = self.connection.cursor()

        try:
            cursor.execute(sql)
            return cursor.fetchall()

        finally:
            cursor.close()

    def close(self):

        self.connection.close()