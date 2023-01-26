
from threading import Thread, Lock
import random
import time

stdout_lock = Lock()

class SimpleThread(Thread):
    def __init__(self, num):
        super().__init__()  # call base class constructor -- REQUIRED
        self._threadnum = num

    def run(self):  # the function that does the work in the thread
        time.sleep(random.randint(1, 3))
        with stdout_lock:
            print("Hello from thread {}".format(self._threadnum))

# animal = 'whelk'

for i in range(10):
    t = SimpleThread(i)  # create the thread
    t.start()  # launch the thread

animal = 'elk'

print("Done.")
