

def multi_thing():
    yield "this"
    yield "is"
    yield "the"
    yield "coolness"
    yield "of"
    yield "Python"
    for i in range(3):
        yield('!')

mt = multi_thing()

for word in mt:
    print(word, end=" ")
print()

mt = multi_thing()

a, b, c, *d, e, f, g = mt
print(a, b, c, d, e, f, g)
