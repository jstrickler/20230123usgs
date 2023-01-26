from functools import wraps
from datetime import datetime
import logging

logging.basicConfig(filename="deco.log", level=logging.INFO)

def bark(func):

    @wraps(func)
    def _(*wombat, **kwargs):
        print("woof! woof!")
        return func(*wombat, **kwargs)

    return _


def add_timestamp(func):

    @wraps(func)
    def _(*args, **kwargs):
        logging.info(f"{func.__name__} called at {datetime.now().strftime('%X: %x')}")
        return func(*args, **kwargs)

    return _

@bark
@add_timestamp
def spam():
    print("SPAM SPAM SPAM")


def ham():
    print("HAM HAM HAM")

ham = add_timestamp(ham)

spam()
ham()
spam()
spam()

print(f"spam.__name__: {spam.__name__}")
print(f"ham.__name__: {ham.__name__}")

def log_timestamp(time_zone):

    def wrapper(old_func):
        @wraps(old_func)
        def _(*args, **kwargs):
            print(f"Using {time_zone}")
            return old_func(*args, **kwargs)
        return _

    return wrapper


@log_timestamp('PDT')
def foo():
    pass

foo()

@log_timestamp('EST')
def bar():
    pass

bar()

# without args
# bar = deco(func)
# with args
# bar = deco(args)(func)

# bar = log_timestamp('EST')(bar)




