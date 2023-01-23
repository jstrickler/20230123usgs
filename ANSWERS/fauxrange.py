
class fauxrange:

    def __init__(self, *values):
        self._start = 0
        self._stop = 0
        self._step = 1
        if len(values) == 1:
            self._stop = values[0]
        elif len(values) == 2:
            self._start = values[0]
            self._stop = values[1]
        elif len(values) == 3:
            self._start = values[0]
            self._stop = values[1]
            self._step = values[2]

    def __next__(self):
        next_value = self._start
        if next_value > self._stop:
            raise StopIteration

        self._start += self._step
        return next_value

    def __iter__(self):
        return self

r1 = fauxrange(10)
print(list(r1))

r2 = fauxrange(1, 11)
print(list(r2))

r3 = fauxrange(5, 101, 5)
print(list(r3))

