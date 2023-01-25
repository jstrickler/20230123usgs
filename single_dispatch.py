from functools import singledispatch

@singledispatch
def calculate(x):
    raise TypeError("can only calculate float or string")

@calculate.register(float)
def _(x):
    return x * 3

@calculate.register(str)
def _(x):
    return ' '.join([x] * 3)


print(calculate(5.0))
print(calculate('wombat'))

def ncalc(x):
    if isinstance(x, [int, float]):
        print("OK")
    else:
        raise TypeError("you are doomed")

def argle(factor: int, file_name: str) -> list[int]:
    print(factor, file_name)

argle(5, 'foo.txt')

argle(10.0, b"abc")









