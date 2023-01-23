from timeit import Timer

REPEATS = 1000000

setup = '''
def F():
    return 1, 2, 3
'''

code_snippets = [
    '*_, x = F()',
    'x = F()[2]',
    't = F();x = t[2]',
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup)
    print("{:60.60s}{}".format(code_snippet, t.timeit(REPEATS)))
    print('-' * 60)
