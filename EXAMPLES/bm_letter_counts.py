from timeit import Timer

setup_code = """
import re
alice_text = open('../DATA/alice.txt').read()
alice_bytes = alice_text.encode()
"""

codes = [
    '''count = alice_text.count('a') + alice_text.count('A')''',
    '''count = alice_text.lower().count('a')''',
    '''count = len(re.findall(r'[aA]', alice_text))''',
    '''count = len(re.findall('a', alice_text, re.I))''',
    '''count = alice_bytes.count(65) + alice_bytes.count(97)''',
]

for code in codes:
    t = Timer(code, setup_code)
    print(code, '\n')
    print(t.timeit(1000))
    print('-' * 60)
