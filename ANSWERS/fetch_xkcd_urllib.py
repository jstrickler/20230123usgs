#!/usr/bin/env python

import sys
from urllib.request import urlopen
from urllib.error import HTTPError

url = 'http://imgs.xkcd.com/comics/python.png'
saved_pdf_file = 'xkcd.png'

try:
    response = urlopen(url)
except HTTPError as err:
    print("Unable to open URL:", err)
    sys.exit(1)

pdf_contents = response.read()
response.close()

with open(saved_pdf_file, 'wb') as xkcd_out:
    xkcd_out.write(pdf_contents)
