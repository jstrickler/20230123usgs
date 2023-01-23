
from timeit import Timer

REPEATS = 1000

setup = '''
list_a = list(range(1, 1000))
list_b = list(range(3, 27)) + list(range(897, 918)) + list(range(1235, 1242))
'''

codes = [
    '[a for a in list_a for b in list_b if a == b]',  # list comprehension
    '{a for a in list_a for b in list_b if a == b}',  # set comprehension
    'set(list_a) & set(list_b)',  # set intersection
]

for code in codes:
    t = Timer(code, setup)
    print("{:60s}{}".format(code, t.timeit(REPEATS)))
    print('-' * 60)
