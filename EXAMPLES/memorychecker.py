import os
import psutil

class MemoryChecker():
    """
    Callable class to get current memory use of program.

    Instances of this class may be called, at which time
    they will return current memory use.
    """

    def __init__(self):
        self.process = psutil.Process(os.getpid())  # Get PID of current process

    def get_usage(self):
        return self.process.memory_info().rss  # Return memory use for PID

if __name__ == '__main__':
    mc = MemoryChecker()
    print(mc.get_usage())  # can call at any time to get current memory use
    x = [0] * 10000000
    print(mc.get_usage())

