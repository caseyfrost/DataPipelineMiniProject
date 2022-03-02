"""
Helper functions for data pipeline
"""

import mysql.connector


def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user='',
                                             password='',
                                             host='localhost',
                                             port='3306',
                                             database='eventsystem')
    except Exception as error:
        print("Error while connecting to database", error)

    return connection


def load_third_party(connection, filepath_to_csv):
    cursor = connection.cursor()
    try:
        pass
        # [Iterate through the CSV file and execute insert statement]
    except Exception as error:
        print("Error encountered while inserting data: ", error)
    connection.commit()
    cursor.close()
    return True


def query_popular_tickets(connection):
    # Get the most popular ticket in the past month
    sql_statement = "<your sql statement>"
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records
