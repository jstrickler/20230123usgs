from multiprocessing.dummy import Pool  # .dummy has Pool for threads
import requests
import time

POOL_SIZE = 8

BASE_URL = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'  # base url of site to access

API_KEY = 'b619b55d-faa3-442b-a119-dd906adc79c8' # credentials to access site

SEARCH_TERMS = [  # terms to search for; each thread will search some of these terms
    'wombat', 'pine marten', 'python', 'pearl',
    'sea', 'formula', 'translation', 'common',
    'business', 'frog', 'muntin', 'automobile',
    'green', 'connect','vial', 'battery', 'computer',
    'sing', 'park', 'ladle', 'ram', 'dog', 'scalpel'
]
def main():
    for function in get_data_threaded, get_data_serial:
        start_time = time.time()
        results = function()
        total_time = time.time() - start_time
        for search_term, result in zip(SEARCH_TERMS, results):  # iterate over results, mapping them to search terms
            results = function()
            print("{}:".format(search_term.upper()), end=" ")
            if result:
                print(result)
            else:
                print("** no results **")
        print("{} took {:.2f} seconds\n".format(function.__name__, total_time))

def fetch_data(term):  # function invoked by each thread for each item in list passed to map()
    try:
        response = requests.get(
            BASE_URL + term,
            params={'key': API_KEY},
        )  # make the request to the site
    except requests.HTTPError as err:
        print(err)
        return []
    else:
        data = response.json()  # convert JSON to Python structure
        parts_of_speech = []
        for entry in data: # loop over entries matching search terms
            if isinstance(entry, dict):
                meta = entry.get("meta")
                if meta:
                    part_of_speech = entry.get("fl")
                    if part_of_speech:
                        parts_of_speech.append(part_of_speech)
        return sorted(set(parts_of_speech))  # return list of parsed entries matching search term


def get_data_threaded():
    p = Pool(POOL_SIZE)  # create pool of POOL_SIZE threads
    return p.map(fetch_data, SEARCH_TERMS)  # launch threads, collect results

def get_data_serial():
    return [fetch_data(w) for w in SEARCH_TERMS]


if __name__ == '__main__':
    main()
