
from timeit import Timer

setup_code = """
d1 = {'a': 5, 'b': 10, 'c': 15}
d2 = {'a': 'wombat', 'b': 'wallaby', 'c': 'koala'}
"""

codes = [
    '''{ x: (d1[x], d2[x]) for x in d1}''',
    '''{ x: (y, d2[x]) for x, y in d1.items()}''',
    '''dict(zip(d1.keys(),zip(d1.values(), d2.values())))''',
]

for code in codes:
    t = Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit())
    print()
