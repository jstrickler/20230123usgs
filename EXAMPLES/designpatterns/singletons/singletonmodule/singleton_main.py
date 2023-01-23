#!/usr/bin/env python
# (c)2015 John Strickler

from dbconn import db_cursor
from builddb import build_database

build_database()

db_cursor.execute(
    '''
        select first_name, last_name
        from computer_people
    '''
)

for row in db_cursor.fetchall():
    print(' '.join(row))
