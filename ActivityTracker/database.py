import sqlite3
from sqlite3 import Error

def create_connection(db_file):

    # create a database connection to SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    # create a table from the create_table_sql statement
    # :param conn: Connection object
    # :param create_table_sql: a CREATE TABLE statement
    # :return:
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"/home/malte/python/ActivityTracker/activities.db"

    sql_create_activities_table = '''CREATE TABLE IF NOT EXISTS activities
             (id INTEGER PRIMARY KEY, date TEXT, type TEXT, distance REAL, duration REAL, 
              average_speed REAL, info TEXT)'''

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_activities_table)
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    create_connection(r"/home/malte/python/ActivityTracker/activities.db")