import pytest

def test_two_plus_two_equals_four():  # tests should begin with "test" (or will not be found automatically)
    assert 2 + 2 == 4   # if assert statement succeeds, the test passes
    assert 3 - 1 == 2, "Math is broken"

def test_something():
    print("Hi, Mom!")
    assert True

def test_x():
    x = 5
    assert x is x


