import sys

color = "blue"

x = "color"

g = globals()

print(f"g[x]: {g[x]}")
print(f"g: {g}")

g['animal'] = "wombat"

print(f"animal: {animal}")

g['bark'] = lambda: print("woof woof")

bark()

tree = "elm"
spam = "fatty pork meat"

def printx(*args, **kwargs):
    __builtins__.print("HA HA Fake print")
    __builtins__.print(*args, **kwargs)

def foo(toast):
    spam = 12
    # local -> nonlocal -> global -> builtin
    print(spam)
    print(tree)
    print(f"locals(): {locals()}")

foo(35)
print(f"spam: {spam}")

def ham():
    print(f"river: {river}")

river = "Nile"

ham()

foo = "megatron"

def alpha(foo):
    bar = 25

    def beta():
        foo = "USGS"
        print(f"foo: {foo}")
        print(f"bar: {bar}")
        return "weirdness"

    return beta

b = alpha(32)
print(f"type(b): {type(b)}")
x = b()
print(f"x: {x}")

u = 1234

def bad_function():
    # 'global' is EVIL and DANGEROUS and BAD and NAUGHTY
    global u, v  # put u in global namespace, not local
    v = "vanilla"
    u = 25
    print(f"in function -- u: {u}")

bad_function()
print(f"in main --  u: {u}")
print(f"in main -- v: {v}")



