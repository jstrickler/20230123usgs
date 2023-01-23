
from timeit import Timer

setup_code = """x = 1000000"""

code_snippets = [
    '''x += 1000000''',
    '''x = x + 1000000''']

for code in code_snippets:
    t = Timer(code, setup_code)
    print(code)
    print(t.timeit())
    print()
