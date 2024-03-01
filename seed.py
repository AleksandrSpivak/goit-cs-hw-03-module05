import logging
from random import randint, choice

from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connect

fake = Faker()

NUMBER_OF_USERS = 100
NUMBER_OF_TASKS = 500


def insert_data_users(conn, sql_stmt):
    """
    Insert data for a NUMBER_OF_USERS into the database using the provided connection and SQL statement.

    Parameters:
    conn (connection): The connection to the database.
    sql_stmt (str): The SQL statement to execute for each user.

    Returns:
    None
    """
    c = conn.cursor()
    email_list = set()
    try:
        for _ in range(NUMBER_OF_USERS):
            fullname = fake.name()
            email = fake.email()
            while email in email_list:
                email = fake.email()
            email_list.add(email)
            c.execute(sql_stmt, (fullname, email))

        conn.commit()
    except DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
        c.close()


def insert_data_status(conn, sql_stmt):
    """
    Function for inserting data status into the database.

    Args:
    conn: Connection object to the database.
    sql_stmt: SQL statement for inserting data status.

    Returns:
    None
    """
    statuses = ["new", "inProgress", "completed"]
    c = conn.cursor()
    try:
        for s in statuses:
            c.execute(sql_stmt, (s,))

        conn.commit()
    except DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
        c.close()


def insert_data_tasks(conn, sql_stmt):
    """
    Insert NUMBER_OF_TASKS data tasks into the database using the provided connection and SQL statement.

    Parameters:
    conn (connection): The connection to the database.
    sql_stmt (str): The SQL statement to insert data into the database.

    Returns:
    None
    """
    tasks_list = [
        "prepare",
        "write",
        "proceed",
        "finish",
        "make",
        "fix",
        "ASAP",
        "Urgent",
        "High",
        "Medium",
        "Low",
        "department",
        "client",
        "project",
        "task",
    ]
    c = conn.cursor()
    try:
        for _ in range(NUMBER_OF_TASKS):
            title = fake.sentence(ext_word_list=tasks_list)
            description = fake.text()
            c.execute(
                sql_stmt,
                (title, description, randint(1, 3), randint(1, NUMBER_OF_USERS)),
            )

        conn.commit()
    except DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
        c.close()


if __name__ == "__main__":

    sql_stmt_status = """
        INSERT INTO status (name) VALUES (%s)
        """

    sql_stmt_users = """
        INSERT INTO users (fullname, email) VALUES (%s, %s)
        """

    sql_stmt_tasks = """
        INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)
        """

    try:
        with create_connect() as conn:
            insert_data_status(conn, sql_stmt_status)
    except RuntimeError as err:
        logging.error(f"Logging error: {err}")

    try:
        with create_connect() as conn:
            insert_data_users(conn, sql_stmt_users)
    except RuntimeError as err:
        logging.error(f"Logging error: {err}")

    try:
        with create_connect() as conn:
            insert_data_tasks(conn, sql_stmt_tasks)
    except RuntimeError as err:
        logging.error(f"Logging error: {err}")
