from copy import deepcopy

alpha = [['a', 'b', 'c'], [1, 2, 3]]
beta = alpha
beta.append(['spam', 'ham', 'toast'])
print(f"alpha: {alpha}")
print(f"beta: {beta}")
# SHALLOW copies
gamma = list(alpha)
gamma = alpha[::]  # entire slice
gamma = alpha.copy()
print(f"id(alpha): {id(alpha)}")
print(f"id(beta): {id(beta)}")
print(f"id(gamma): {id(gamma)}")
gamma.append(['foo', 'bar', 'baz'])
print(f"alpha: {alpha}")
print(f"beta: {beta}")
print(f"gamma: {gamma}")
print(f"alpha is beta: {alpha is beta}")
print(f"alpha is gamma: {alpha is gamma}")
gamma[0].append('d')
print(f"alpha: {alpha}")
print(f"beta: {beta}")
print(f"gamma: {gamma}")
print("\U0001F92F")
delta = deepcopy(alpha)
delta[2].append('eggs')
print(f"alpha: {alpha}")
print(f"beta: {beta}")
print(f"gamma: {gamma}")
print(f"delta: {delta}")

def doit(mydata):
    print(mydata)

doit(gamma)
