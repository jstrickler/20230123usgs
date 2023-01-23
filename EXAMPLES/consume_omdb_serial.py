from omdblib import OMDB

def get_ratings(movie_titles):
    omdb = OMDB("b87452b6")

    ratings = []
    for title in movie_titles:
        movie = omdb.title_search(title)
        ratings.append(movie.rotten_tomatoes_score)
    return ratings




