"""
Helper functions for data pipeline
"""

import mysql.connector


def load_third_party(connection, filepath_to_csv):
    cursor = connection.cursor()
    try:
        # [Iterate through the CSV file and execute insert statement]
        sql = "INSERT INTO ticket_sales(ticket_id,trans_date,event_id,event_name,event_date,event_type,event_city," \
              "customer_id,price,num_tickets) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); "
        cur = connection.cursor()
        with open(filepath_to_csv) as file:
            for line in file.readlines():
                row = tuple(line.strip().split(','))
                cur.execute(sql, row)
        connection.commit()
        cur.close()

    except Exception as error:
        print("Error encountered while inserting data: ", error)
    finally:
        cursor.close()
    return True


def query_popular_tickets(connection):
    # Get the most popular ticket in the past month
    sql_statement = "SELECT event_name FROM ticket_sales WHERE MONTH(event_date) = 9 ORDER BY num_tickets DESC"
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records


def print_records(records):
    print("Here are the most popular events last month: ")
    for record in records:
        print(f"    - {record[0]}")
