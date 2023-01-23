#!/usr/bin/env python
# (c)2015 John Strickler

import sqlite3

class DatabaseConnection(object):
    _shared = {}

    def __new__(cls, *args, **kwargs):
        instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)

        if not '_db_connection' in cls._shared:
            db_conn = sqlite3.connect(':memory:')
            db_cursor = db_conn.cursor()

            cls._shared['_db_connection'] = db_conn
            cls._shared['_db_cursor'] = db_cursor

        instance.__dict__ = cls._shared


        return instance

    @property
    def cursor(self):
        return self._db_cursor
