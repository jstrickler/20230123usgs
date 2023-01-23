import scipy as sp

p1 = sp.poly1d([2, 1, 4])  # 2,1,4 are coefficients
print(p1)
print()

print(p1(.75))  # evaluate for x = .75

print(p1.r)  # get the roots
print()

p2 = sp.poly1d([2, 1, -4], True)  # 2,1,-4 are roots
print(p2)
print()

print(p2(.75))  # evaluate for x = .75
print(p2.r)  # get the roots
print()

p3 = sp.poly1d([1, 2, 3], False, 'm')  # 1,2,3 are coefficients, variable is 'm'
print(p3)
print()

print(p3(100))  # evaluate for m = 100

print(p3.r)  # get the roots
print()

p4 = sp.poly1d([1, 2])  # polynomial arithmetic
p5 = sp.poly1d([3, 4])
print()

print(p4)
print()

print(p5)
print()

print(p4 + p5)
print()

print(p4 - p5)
print()

print(p4 ** 3)
print()
