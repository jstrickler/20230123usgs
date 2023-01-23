import time
from functools import partial
from multiprocessing import Pool
from omdblib import OMDB

def get_rt_score(omdb, title):
    movie = omdb.title_search(title)
    return movie.rotten_tomatoes_score

def get_ratings(movie_titles):
    omdb = OMDB("b87452b6")
    process_pool = Pool(processes=16)

    get_score = partial(get_rt_score, omdb)
    ratings = process_pool.map(get_score, movie_titles)
    return ratings



