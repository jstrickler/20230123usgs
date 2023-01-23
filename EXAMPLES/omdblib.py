from dataclasses import dataclass
import requests
import aiohttp


@dataclass
class Movie:
    title: str
    year: int
    director: str
    plot: str
    rotten_tomatoes_score: int

class OMDB:
    OMDB_URL = "http://www.omdbapi.com"

    def __init__(self, api_key):
        self.api_key = api_key

    def title_search(self, title, *, full_plot=False):
        return self._single_search(title, "t", full_plot)

    def imdb_id_search(self, imdb_id, *, full_plot=False):
        return self._single_search(imdb_id, "i", full_plot)

    def _single_search(self, search_key, search_param, full_plot):
        raw_data = self._fetch_data(search_key, search_param, full_plot)
        return self._parse_movie(raw_data)

    def keyword_search(self, keyword, *, full_plot=False):
        raw_data = self._fetch_data(keyword, 's', full_plot)
        return self._parse_movies(raw_data)

    def _parse_movies(self, raw_data):
        movies = []
        for movie_data in raw_data['Search']:
            if 'imdbID' in movie_data:
                movies.append(self.imdb_id_search(movie_data['imdbID']))

        return movies

    def _fetch_data(self, search_key, search_param, full_plot):
        """
        Fetch data from OMDB api using requests.

        :param search_key: text to find (title, imdb_id, or partial title)
        :param search_param: 'i' for imdb_id, 't' for title, or 's' for search
        :param full_plot: True to request full plot
        :return:
        """
        requests_params = {search_param: search_key, "apikey": self.api_key}

        if full_plot:
            requests_params['plot'] = 'full'

        response = requests.get(
            self.OMDB_URL,
            params=requests_params,
        )

        if response.status_code == requests.codes.OK:
            raw_data = response.json()  # import json; raw_data = json.load(response.text)
        else:
            raise Exception(f"Request failed: {response.status_code}")

        return raw_data

    def _parse_movie(self, raw_data):
        rt_rating = None
        if 'Ratings' in raw_data:
            for rating in raw_data['Ratings']:
                if rating.get('Source') == "Rotten Tomatoes":
                    rt_rating = int(rating['Value'].rstrip('%'))
                    break
        movie = Movie(
            raw_data.get('Title'),
            raw_data.get('Year'),
            raw_data.get('Director'),
            raw_data.get('Plot'),
            rt_rating,
        )
        return movie


class OMDBasync(OMDB):
    """
    Async version of OMDB

    API calls require a parameter of type aiohttp.ClientSession()

    """
    def title_search(self, title, session, *, full_plot=False):
        return self._single_search(title, "t", session, full_plot)

    def imdb_id_search(self, imdb_id, session, *, full_plot=False):
        return self._single_search(imdb_id, "i", session, full_plot)

    async def _single_search(self, search_key, search_param, session, full_plot):
        raw_data = await self._fetch_data(search_key, search_param, session, full_plot)
        return self._parse_movie(raw_data)

    def keyword_search(self, keyword, session, full_plot=False):
        return self._multi_search(keyword, session, full_plot)

    async def _multi_search(self, search_key, session, full_plot):
        raw_data = await self._fetch_data(search_key, 's', session, full_plot)

        movies = []
        for movie_data in raw_data['Search']:
            if 'imdbID' in movie_data:
                movies.append(await self.imdb_id_search(movie_data['imdbID'], session))

        return movies

    async def _fetch_data(self, search_key, search_param, session, full_plot):
        """
        Fetch data from OMDB api using async

        :param search_key: text to find (title, imdb_id, or partial title)
        :param search_param: 'i' for imdb_id, 't' for title, or 's' for search
        :param full_plot: True to request full plot
        :return:
        """
        url = self._make_url(search_param, search_key, full_plot)

        async with session.get(url) as response:
            raw_data = await response.json()
            return raw_data

    def _make_url(self, search_param, search_key, full_plot):
        params = {search_param: search_key, "apikey": self.api_key}
        if full_plot:
            params['plot'] = 'full'

        param_string = '?' + '&'.join(f"{k}={v}" for k, v in params.items()).replace(' ', '+')
        return self.OMDB_URL + param_string






if __name__ == '__main__':
    import asyncio

    def display_movie(m):
        print(f"{m.title} ({m.year}): {m.director}")
        print('-' * len(m.title))
        print(m.plot, '\n')


    omdb = OMDB('b87452b6')

    m1 = omdb.title_search("The GodFather", full_plot=True)
    display_movie(m1)

    m2 = omdb.imdb_id_search("tt3896198", full_plot=True)
    display_movie(m2)

    print("=" * 60)
    print("=" * 60)

    movie_list = omdb.keyword_search('nerds')
    for movie in movie_list:
        display_movie(movie)
        print("-" * 10)

    print("*" * 60)
    print("*" * 60)

    omdb = OMDBasync('b87452b6')

    async def doit():

        async with aiohttp.ClientSession() as session:
            movie_list = await omdb.keyword_search('nerds', session, full_plot=True)
            for movie in movie_list:
                display_movie(movie)
                print('-' * 10)

    asyncio.run(doit())
