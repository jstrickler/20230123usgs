from timeit import Timer

setup_code = """
values = []
"""  # setup code is only executed once

test_code_one = '''
for i in range(10000):
    values.append(i)
values.clear()
'''  # code fragment executed many times

test_code_two = '''
i = 0
while i < 10000:
    values.append(i)
    i += 1
values.clear()
'''  # code fragment executed many times

t1 = Timer(test_code_one, setup_code)  # Timer object creates time-able code
t2 = Timer(test_code_two, setup_code)  # Timer object creates time-able code

print("test one:")
print(t1.timeit(1000))  # timeit() runs code fragment N times
print()

print("test two:")
print(t2.timeit(1000))  # timeit() runs code fragment N times
print()
