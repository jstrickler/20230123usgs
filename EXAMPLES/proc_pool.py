
import random
from multiprocessing import Pool

POOL_SIZE = 32  # number of processes

with open('../DATA/words.txt') as words_in:
    WORDS = [w.strip() for w in words_in]  # read word file into a list, stripping off 


random.shuffle(WORDS)  # randomize word list


def my_task(word):  # actual task
    return word.upper()


if __name__ == '__main__':
    ppool = Pool(POOL_SIZE)  # create pool of POOL_SIZE processes

    WORD_LIST = ppool.map(my_task, WORDS)  # pass wordlist to pool and get results; map assigns values from input list to processes as needed

    print(WORD_LIST[:20])  # print last 20 words

    print("Processed {} words.".format(len(WORD_LIST)))
