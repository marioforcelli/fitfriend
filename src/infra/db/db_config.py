import psycopg2
import os
from psycopg2.extras import RealDictCursor

from src.domain.exceptions.user import UserAlreadyExistsError

DEFAULT_DB_CONFIG = {
    "dbname": os.environ.get("POSTGRES_DB", None),
    "user": os.environ.get("POSTGRES_USER", None),
    "password": os.environ.get("POSTGRES_PASSWORD", None),
    "host": os.environ.get("POSTGRES_HOST", "localhost"),
    "port": os.environ.get("POSTGRES_PORT", 5434),
}


class Database:
    def __init__(self, db_config=DEFAULT_DB_CONFIG):
        self.connection = psycopg2.connect(**db_config)

        if self.connection is None:
            raise ConnectionError("Failed to connect to the database")

        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        try:

            with self.connection.cursor() as cursor:

                a = cursor.execute(query, params)
                id = cursor.fetchone()[0]
                print(id)
                return a
        except psycopg2.errors.UniqueViolation:
            print("Unique constraint violated")
            raise UserAlreadyExistsError
        except Exception as e:
            # self.cursor.rollback()
            self.close()
            print(f"Error executing query: {e}")
            raise

    def fetch_one(self, query, params=None):
        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()
        except Exception as e:
            print(f"Error fetching one: {e}")
            raise

    def fetch_all(self, query, params=None):
        try:
            with self.connection.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching all: {e}")
            raise

        except Exception as e:
            self.connection.rollback()
            raise

    def close(self):
        self.cursor.close()
        self.connection.close()
