import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
     '''
        Load each staging table with copy command. 
    '''
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    '''
        Insert the data into fact and dimension tables. 
    '''
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
         '''
        - Establishes connection with the dwh database and gets
         cursor to it.  
    
        - Load all the staging tables.  
    
        - Insert into all tables needed. 
    
        - Finally, closes the connection. 
    '''
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()