

def coroutine():  # Define a coroutine function
    in_value = ''
    while True:
        in_value = yield in_value.upper()  # Yield gets the result of send() AND provides the next value
        print('in_value:', in_value)


c = coroutine()  # Create instance of coroutine

print(c)  # c is a coroutine object (also a generator)
print(next(c))  # next() will get the next value and prime the coroutine. You _must_ call next before calling send()
print()

for letter in "alpha", "beta", 'gamma':
    print("out_value:", c.send(letter))  # Send a value to the coroutine
print()


def faux_range():  # define a generator
    i = 0
    while i < 4:
        yield i
        i += 1


def spam():
    yield from faux_range()  # Define generator; yield from _delegates_ to another generator


s = spam()  # Create instance of generator

for x in s:  # Looping through a spam() instance effictively loops over faux_range()
    print(x)
