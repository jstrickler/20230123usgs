
from timeit import Timer

REPEATS = 10000

setup = '''
import random
nums = [random.randint(1,100) for _ in range(10000000)]
'''


code_snippets = [
    '''
' '.join([str(n) for n in nums])
    ''',
    '''
' '.join(str(n) for n in nums)
    ''',
]

for snippet in code_snippets:
    t = Timer(snippet, setup)
    print("{:60.60s}{}".format(snippet, t.timeit(REPEATS)))
    print('-' * 60)
