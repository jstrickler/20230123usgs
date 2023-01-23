import time
import py_primes
import numba_primes
import pyximport

pyximport.install() # autocompile cython code
import cy_primes # import three modules that have a primes() function

NUM_PRIMES = 100000 # set upper limit for finding primes

for mod in numba_primes, cy_primes, py_primes: # loop through modules

    timestamp = time.time() # get starting timestamp

    prime_list = mod.get_primes(NUM_PRIMES)  # call primes() function

    timestamp2 = time.time() # get ending timestamp

    elapsed = timestamp2 - timestamp  # calculate elapsed time

    print(prime_list[:20], prime_list[-20:])

    print("{} took {:.3f} seconds to find {} primes".format(
        mod.__name__, elapsed, len(prime_list))) # display results
    print()
