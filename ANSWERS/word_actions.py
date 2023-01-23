#!/usr/bin/env python
from collections import defaultdict

class WordSelect():
    function_registry = defaultdict(list) # dict of (min_len, max_len):[func_list] pairs

    def __call__(self, min_len, max_len):
        """
        Decorator for word-processing functions. Apply to functions to select words of specified lengths.

        :param min_len: Minimum word length for the decorated function
        :param max_len: Maximum word length for the decorated function
        :return: wrapper ("real" decorator)
        """

        def wrapper(old_function):
            """
            Register function with corresponding max/min values

            :param old_function: function to be registered
            :return: replacement function (actually original function)
            """
            # add function to registry indexed by min_len, max_len
            self.function_registry[(min_len, max_len)].append(old_function)

            return old_function # no changes needed

        return wrapper

    def process_words(self):
        """
        Process the list of words from the words.txt file.

        For each word, check to see if the length is within the range for each
        list of functions. If so, call all the functions for the word and print the result.

        :return: None. Note: could return list of words, rather than printing them
        """
        with open('../DATA/words.txt') as words_in:
            for raw_word in words_in:
                word = raw_word.rstrip()
                word_len = len(word)
                for (min_len, max_len), word_functions in self.function_registry.items():
                    if (word_len >= min_len) and (word_len <= max_len):
                        for word_function in word_functions:
                            result = word_function(word)
                            print(result)

word_select = WordSelect() # create (callable) instance of class

@word_select(16, 18)
def make_upper(s):
    return s.upper()

@word_select(18, 20)
def reverse_word(s):
    return s[::-1]

@word_select(22, 22)
def add_stars(s):
    return '*** ' + s

@word_select(1, 2)
def times_10(s):
    return "-".join([s] * 10)

word_select.process_words()
