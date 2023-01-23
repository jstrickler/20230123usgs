import threading  # see multiprocessing.dummy.Pool for the easier way
import random
import time

WORDS = 'apple banana mango peach papaya cherry lemon watermelon fig elderberry'.split()

MAX_SLEEP_TIME = 3
WORD_LIST = []  # the threads will append words to this list
WORD_LIST_LOCK = threading.Lock()  # generic locks
STDOUT_LOCK = threading.Lock()  # generic locks

class SimpleThread(threading.Thread):
    def __init__(self, num, word):  # thread constructor
        super().__init__()  # be sure to call parent constructor
        self._word = word
        self._num = num

    def run(self):  # function invoked by each thread
        time.sleep(random.randint(1, MAX_SLEEP_TIME))

        with STDOUT_LOCK:  # acquire lock and release when finished
            print("Hello from thread {} ({})".format(self._num, self._word))

        with WORD_LIST_LOCK:  # acquire lock and release when finished
            WORD_LIST.append(self._word.upper())

all_threads = []  # make list ("pool") of threads (but see Pool later in chapter)
for i, random_word in enumerate(WORDS, 1):
    t = SimpleThread(i, random_word)  # create thread
    all_threads.append(t)  # add thread to "pool"
    t.start()  # start thread

print("All threads launched...")

for t in all_threads:
    t.join()  # wait for thread to finish

print(WORD_LIST)
