from collections.abc import Sized, Iterator  # Abstract base classes, used similarly to interfaces in Java or C#


class BadContainer(Sized):  # This class may not be instantiated without defining `len()`
    pass


class GoodContainer(Sized):
    def __len__(self):   # This class is fine, since `Sized` requires `len()` to be implemented
        return 42


try:
    bad = BadContainer()  # Instantiating `BadContainer` raises an error.
except TypeError as err:
    print(err)
else:
    print(bad)

print()

try:
    good = GoodContainer()  # Instantiating `GoodContainer` is fine
except TypeError as err:
    print(err)
else:
    print(good)
    print(len(good))  # Builtin function `len()` works with all objects that inherit from `Sized` (due to implementation of `len())`

print()


class MyIterator(Iterator):  # ABC `Iterator` provides abstract method `next`
    data = 'a', 'b', 'c'
    index = 0

    def __next__(self):  # Must be implemented for Iterators
        if self.index >= len(self.data):
            raise StopIteration
        else:
            return_val = self.data[self.index]
            self.index += 1
            return return_val


m = MyIterator()  # Create instance of `MyIterator`
for i in m:  # Iterate over the iterator instance
    print(i)
print()

print(hasattr(m, '__iter__'))  # Check to see if `m` is iterable
