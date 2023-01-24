

def multiply(x, y):
    return x * y

print(multiply(8, 9))

a = 10
b = 32
print(multiply(a, b))

nums = [21, 2]
print(multiply(*nums))



def do_config(**config_info = {
    'file': 'spam.txt',
    'user': 'xerxes1',
}args):
    print(args)

do_config(name='Bob', file="ham.txt", country="Burkina Faso")

do_config(**config_info)

def spam(*args, **kwargs):
    pass

