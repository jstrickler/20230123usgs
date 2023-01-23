from collections import namedtuple
import pytest

Person = namedtuple('Person', 'first_name last_name')  # create object to test

FIRST_NAME = "Guido"
LAST_NAME = "Von Rossum"

@pytest.fixture  # mark person as a fixture
def person():
    """
    Return a 'Person' named tuple with fields 'first_name' and 'last_name'
    """
    return Person(FIRST_NAME, LAST_NAME)  # return value of fixture


def test_first_name(person):  # pass fixture as test parameter
    assert person.first_name == FIRST_NAME

def test_last_name(person):  # pass fixture as test parameter
    assert person.last_name == LAST_NAME

