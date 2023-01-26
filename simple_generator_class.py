

class abc_forever:
    def __init__(self):
        self.index = 0
        self.values = 'A', 'B', 'C'

    def __iter__(self):
        return self

    def __next__(self):  # respond to next()
        if self.index == 3:
#            self.index = 0
            raise StopIteration()
        value = self.values[self.index]
        self.index += 1
        return value

x = abc_forever()
for value in x:
    print(value)
for value in x:
    print(value)

x = abc_forever()
it = iter(x)
print(type(it))
print(next(it))
print(next(it))

x = abc_forever()
it = iter(x)
for value in it:
    print(value)
