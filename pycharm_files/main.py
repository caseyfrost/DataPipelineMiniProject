import utilities
import connect


if __name__ == '__main__':
    csv_path = r'your path goes here'
    con = connect.connect()
    ins = utilities.load_third_party(con, csv_path)
    records = utilities.query_popular_tickets(con)
    utilities.print_records(records)
