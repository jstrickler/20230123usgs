#!/usr/bin/env python
# (c)2015 John Strickler

from databaseconnection import DatabaseConnection

from builddb import build_database

build_database()

db_conn = DatabaseConnection()

db_conn.cursor.execute(
    '''
        select first_name, last_name
        from computer_people
    '''
)

for row in db_conn.cursor.fetchall():
    print(' '.join(row))
