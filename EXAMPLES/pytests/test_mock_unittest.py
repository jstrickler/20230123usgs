import pytest
from unittest.mock import Mock

ham = Mock()  # Create mock version of ham() function


# system under test
class Spam():  # System (class) under test
    def __init__(self, param):
        self._value = ham(param)  # Calls ham() (doesn't know if it's fake)

    @property
    def value(self):  # Property to return result of ham()
        return self._value

# dependency to be mocked -- not used in test
# def ham(n):
#     pass

def test_spam_calls_ham():   # Actual unit test
    _ = Spam(42)  # Create instance of Spam, which calls ham()
    ham.assert_called_once_with(42)  # Check that spam.value correctly returns return value of ham()


if __name__ == '__main__':
    pytest.main([__file__])
