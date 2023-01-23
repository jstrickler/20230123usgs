
class Spam():

    def eggs(self, msg):  # create attribute
        print("eggs!", msg)


s = Spam()

s.eggs("fried")

print("hasattr()", hasattr(s, 'eggs'))  # check whether attribute exists

e = getattr(s, 'eggs')  # retrieve attribute
e("scrambled")


def toast(self, msg):
    print("toast!", msg)


setattr(Spam, 'eggs', toast)  # set (or overwrite) attribute

s.eggs("buttered!")

delattr(Spam, 'eggs')  # remove attribute

try:
    s.eggs("shirred")
except AttributeError as err:  # missing attribute raises error
    print(err)
