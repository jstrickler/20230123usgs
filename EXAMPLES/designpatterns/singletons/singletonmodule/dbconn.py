#!/usr/bin/env python
# (c)2015 John Strickler

# only one connection and one cursor will be created

import sqlite3

db_connection = sqlite3.connect(':memory:')

db_cursor = db_connection.cursor()

