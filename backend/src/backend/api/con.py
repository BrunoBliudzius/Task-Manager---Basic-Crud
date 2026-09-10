import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    try:
        with psycopg2.connect(DATABASE_URL) as connection:
            yield connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise
    finally:
        connection.close()
