import time
from functools import wraps

def functiontimer(function):

    @wraps(function)
    def _(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        elapsed = round(end - start, 3)
        print("Execution of {}() took {} seconds".format(
            function.__name__, elapsed
        ))
        return result

    return _

if __name__ == '__main__':

    @functiontimer
    def spam(maximum=100):
        total = 0
        for i in range(maximum):
            total += i

        return total


    spam()
    spam(10000)
    spam(1000000)

    @functiontimer
    def word_search(pattern):
        found = []
        with open('../DATA/words.txt') as words_in:
            for raw_line in words_in:
                if pattern in raw_line:
                    found.append(raw_line.rstrip())
        return found

    for word in 'wolverine', 'pancreas', 'diphthong', 'ammonia':
        found_words = word_search(word)
        print(found_words)
