#!/usr/bin/python
 
import string
import random
import psycopg2
from config import config

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def insert_col(col_str_one, col_str_two):
    """ insert a new column into debugger table """ 
    sql = """INSERT INTO debugger(col_str_one, col_str_two) VALUES(%s, %s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (col_str_one,col_str_two))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return

if __name__ == '__main__':
    key = id_generator(5)
    value = id_generator(10)
    insert_col(key, value)