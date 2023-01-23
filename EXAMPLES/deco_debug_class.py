

class debugger():  # class implementing decorator

    function_calls = []

    def __init__(self, func):  # original function passed into decorator's constructor
        self._func = func

    def __call__(self, *args, **kwargs):  # __call__() is replacement function

        # print("*" * 40)  # add useful features to original function
        # print("function {}()".format(self._func.__name__))  # add useful features to original function
        # print("\targs are ", args)  # add useful features to original function
        # print("\tkwargs are ", kwargs)  # add useful features to original function
        #
        # print("*" * 40)  # add useful features to original function

        self.function_calls.append(  # add function name and arguments to saved list
            (self._func.__name__, args, kwargs)
        )

        result = self._func(*args, **kwargs)  # call the original function
        return result # return result of calling original function

    @classmethod
    def get_calls(cls): # define method to get saved function call information
        return cls.function_calls

@debugger  # apply debugger to function
def hello(greeting, whom="world"):
    print("{}, {}".format(greeting, whom))

@debugger  # apply debugger to function
def bark(bark_word, *, repeat=2):
    print("{0}! ".format(bark_word) * repeat)

hello('hello', 'world')  # call replacement function
print()

hello('hi', 'Earth')
print()

hello('greetings')

bark("woof", repeat=3)
bark("yip", repeat=4)
bark("arf")

hello('hey', 'girl')

print('-' * 60)

for i, info in enumerate(debugger.get_calls(), 1):  # display function call info from class
    print("{:2d}. {:10s} {!s:20s} {!s:20s}".format(i, info[0], info[1], info[2]))
