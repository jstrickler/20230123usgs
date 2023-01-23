"""
Fetch a word definition from Merriam-Webster's API
"""
import sys
from urllib.request import Request, urlopen
import json
# from pprint import pprint

DATA_TYPE = 'application/json'

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8'

URL_TEMPLATE = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}'  # base URL of resource site

def main(args):
    if len(args) < 1:
        print("Please specify a word to look up")
        sys.exit(1)

    search_term = args[0].replace(' ', '+')

    url = URL_TEMPLATE.format(search_term, API_KEY)  # build search URL

    do_query(url)

def do_query(url):
    print("URL:", url)
    request = Request(url)
    response = urlopen(request)  # send HTTP request and get HTTP response
    raw_json_string = response.read().decode()  # read content from web site and decode() from bytes to str
    data = json.loads(raw_json_string)  # convert JSON string to Python data structure
    # print("RAW DATA:")
    # pprint(data)
    for entry in data:  # iterate over each entry in results
        if isinstance(entry, dict):
            meta = entry.get("meta") # retrieve items from results (JSON convert to lists and dicts)
            if meta:
                part_of_speech = '({})'.format(entry.get('fl'))
                word_id = meta.get("id")
                print("{} {}".format(word_id.upper(), part_of_speech))
            if "shortdef" in entry:
                print('\n'.join(entry['shortdef']))
            print()
        else:
            print(entry)
if __name__ == '__main__':
    main(sys.argv[1:])
