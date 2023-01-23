
class Spam():  # create normal class

    def __init__(self, name):
        self._name = name

    def eggs(self):  # add normal method
        print("Good morning, {}. Here are your delicious fried eggs.".format(self._name, ))


s = Spam('Mrs. Higgenbotham')  # create instance of class
s.eggs()  # call method


def scrambled(self):  # define new method outside of class
    print("Hello, {}. Enjoy your scrambled eggs".format(self._name, ))


setattr(Spam, "eggs", scrambled)  # monkey patch the class with the new method

s.eggs()  # call the monkey-patched method from the instance
