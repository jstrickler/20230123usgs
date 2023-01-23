import time
import asyncio
import aiohttp
from omdblib import OMDBasync

async def get_rt_score(title, session, omdb):
    movie = await omdb.title_search(title, session=session)
    return movie.rotten_tomatoes_score


async def get_ratings(movie_titles):
    async with aiohttp.ClientSession() as session:
        omdb = OMDBasync("b87452b6")
        tasks = []
        for title in movie_titles:
            tasks.append(asyncio.ensure_future(get_rt_score(title, session, omdb)))

        ratings = await asyncio.gather(*tasks)
        return ratings

