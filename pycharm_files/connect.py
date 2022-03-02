import mysql.connector
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the MySQL database...')
        conn = mysql.connector.connect(**params)

        # return the connection object
        return conn
        
    except Exception as error:
        print("An error occured while connecting: ", error)


if __name__ == '__main__':
    connect()
