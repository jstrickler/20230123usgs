import pytest  # Needed for test runner
import re  # Needed for test (but will be mocked)

class SpamSearch():  # System under test
    def __init__(self, search_string, target_string):
        self.search_string = search_string
        self.target_string = target_string


    def findit(self):  # Specific method to test (uses re.search)
        return re.search(self.search_string, self.target_string)

def test_spam_search_calls_re_search(mocker):   # Unit test
    mocker.patch('re.search')  # Patch re.search (i.e., replace re.search with a Mock object that records calls to it)
    s = SpamSearch('bug', 'lightning bug')  # Create instance of SpamSearch
    _ = s.findit()   # Call the method under test
    re.search.assert_called_once_with('bug', 'lightning bug')  # Check that method was called just once with the expected parameters

if __name__ == '__main__':
    pytest.main([__file__, '-s'])   # Start the test runner
