# Code that creates the datatabase and call the sql_queries.py to produce the tables.

import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    DESCRIPTION:
        This function is used to connect to the database 'studentdb'.
        It drops any other database created before with the name 'sparkifydb'.
        And recreate the database for this project.
        In the end, closes the connection with 'studentdb' to maintain only 'sparkifydb'.

    ARGUMENTS:
        none.

    RETURNS:
        conn: Connection to the database;
        cur: Command to execute queries and others in the database session.
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    DESCRIPTION:
        This function drops any other database created before with the name 'sparkifydb'.

    ARGUMENTS:
        cur: Command to execute queries and others in the database session;
        conn: Connection to the database.

    RETURNS:
        None.
    """
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    DESCRIPTION:
        This function creates the tables for the db.

    ARGUMENTS:
        cur: Command to execute queries and others in the database session;
        conn: Connection to the database.

    RETURNS:
        None.
    """
    
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
    