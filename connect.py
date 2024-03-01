import psycopg2
from contextlib import contextmanager


@contextmanager
def create_connect():
    """
    Context manager for creating a connection to the PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(
            host="localhost", database="hw-03", user="postgres", password="12345678"
        )
        try:
            yield conn
        finally:
            conn.close()
    except psycopg2.OperationalError:
        print("Connection failed")
