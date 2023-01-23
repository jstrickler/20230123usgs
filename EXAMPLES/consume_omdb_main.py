import asyncio
import time

from nfrtitles import get_nfr_title_list
import consume_omdb_threads
import consume_omdb_procs
import consume_omdb_cf_threads
import consume_omdb_cf_procs
import consume_omdb_async
import consume_omdb_serial

MODULES = (
    consume_omdb_threads,
    consume_omdb_procs,
    consume_omdb_cf_threads,
    consume_omdb_cf_procs,
    consume_omdb_async,
    consume_omdb_serial,
)

def main():

    movie_titles = get_nfr_title_list()

    for module in MODULES:
        print(f"{module.__name__:25s}", end=" ")
        start_time = time.time()
        if module.__name__ == 'consume_omdb_async':
            ratings = asyncio.run(module.get_ratings(movie_titles))
        else:
            ratings = module.get_ratings(movie_titles)
        total_time = time.time() - start_time

        # print(ratings, '\n')
        print(f"length: {len(ratings)} total time: {total_time:6.2f}")

if __name__ == '__main__':
    main()
