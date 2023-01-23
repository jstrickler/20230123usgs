#!/usr/bin/env python
import webbrowser
import os

file_path = os.path.abspath('../DATA/where_do_i_go.html/')

webbrowser.open('file://' + file_path)
