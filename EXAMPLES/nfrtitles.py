import requests
from bs4 import BeautifulSoup

URL = "https://www.loc.gov/programs/national-film-preservation-board/film-registry/complete-national-film-registry-listing/"

def get_nfr_title_list():
    response = requests.get(URL)
    if response.status_code == requests.codes.OK:
        movies = []
        soup = BeautifulSoup(response.text, "lxml")
        for movie in soup.findAll('th', scope="row"):
            movies.append(movie.text)
        return movies

if __name__ == '__main__':
    movies = get_nfr_title_list()
    print(f"{len(movies)} movies added")
