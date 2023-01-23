import requests
from pprint import pprint

API_KEY = 'b87452b6'

OMDB_URL = "http://www.omdbapi.com"

MOVIE_TITLES = [
    'Black Panther',
    'Frozen',
    'Top Gun: Maverick',
    'Bullet Train',
    'Death on the Nile',
    'Casablanca',
]

def main():
    with requests.Session() as session:
        session.params.update({"apikey": API_KEY})
        for movie_title in MOVIE_TITLES:
            params = {'t': movie_title}
            response = session.get(OMDB_URL, params=params)
            if response.status_code == requests.codes.OK:
                raw_data = response.json()
                print(f"raw_data['Title']: {raw_data['Title']}")
                print(f"raw_data['Director']: {raw_data['Director']}")
                print(f"raw_data['Year']: {raw_data['Year']}")
                print(f"raw_data['Runtime']: {raw_data['Runtime']}")
                print()



if __name__ == '__main__':
    main()
