#!/usr/bin/env python
# (c) 2018 CJ Associates
#
import requests

URL = "https://www.wikipedia.org/"

response = requests.get(URL)

if response.status_code == requests.codes.OK:
    link_count = response.text.count('href')
    print("There are {} links on the Wikipedia main page".format(link_count))
else:
    print("Unable to connect to {}".format(URL), response.reason)
