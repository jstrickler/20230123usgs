
from timeit import Timer

REPEATS = 1000000

setup = '''

'''

code_snippets = [
    '''
''',

    '''
''',
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup)
    print("{:60.60s}{}".format(code_snippet, t.timeit(REPEATS)))
    print('-' * 60)
