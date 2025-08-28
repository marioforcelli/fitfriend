import psycopg2
import os

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
            return False

        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()
