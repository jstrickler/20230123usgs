import requests
from pprint import pprint

API_KEY = 'b87452b6'

OMDB_URL = "http://www.omdbapi.com"

def main():
    requests_params = {'t': 'Black Panther', "apikey": API_KEY}
    response = requests.get(OMDB_URL, params=requests_params)
    if response.status_code == requests.codes.OK:
        raw_data = response.json()

        print(f"raw_data['Title']: {raw_data['Title']}")
        print(f"raw_data['Director']: {raw_data['Director']}")
        print(f"raw_data['Year']: {raw_data['Year']}")
        print(f"raw_data['Runtime']: {raw_data['Runtime']}")
        print()

        print('-' * 60)

        print("raw DATA:")
        pprint(response.json())
    else:
        print(f"response.status_code: {response.status_code}")

if __name__ == '__main__':
    main()
