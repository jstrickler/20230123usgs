#!/usr/bin/env python
# (c) 2018 CJ Associates
#
from urllib.request import urlopen

URL = "https://www.wikipedia.org/"

link_count = 0

with urlopen(URL) as url_in:
    page_content = url_in.read().decode()  # convert from bytes to string

start = 0
while True:
    pos = page_content.find('href', start)
    if pos == -1:  # no more strings
        break
    start = pos + 1
    link_count += 1

print("There are {} links on the Wikipedia main page".format(link_count))
