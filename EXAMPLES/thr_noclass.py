
from threading import Thread, Lock
import random
import time

STDOUT_LOCK = Lock()

def my_task(num):  # function to launch in each thread
    time.sleep(random.randint(1, 3))
    with STDOUT_LOCK:
        print("Hello from thread {}".format(num))


for i in range(10):
    t = Thread(target=my_task, args=(i,))  # create thread
    t.start()  # launch thread

print("Done.")  # "Done" is printed immediately -- the threads are "in the background"
