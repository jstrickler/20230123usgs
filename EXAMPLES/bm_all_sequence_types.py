
from timeit import Timer

REPEATS = 10000000

setup = '''
from array import array
nums = range(100)

x_list = list(nums)
x_tuple = tuple(nums)
x_bytes = bytes(nums)
x_str = x_bytes.decode()
x_array = array('B', nums)
'''

code_snippets = [
    '''
for i in x_list:
    pass
    ''',
    '''
for i in x_tuple:
    pass
    ''',
    '''
for i in x_bytes:
    pass
    ''',
    '''
for i in x_str:
    pass
    ''',
    '''
for i in x_array:
    pass
    ''',
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup)
    print("{:60.60s}{}".format(code_snippet, t.timeit(REPEATS)))
    print('-' * 60)
