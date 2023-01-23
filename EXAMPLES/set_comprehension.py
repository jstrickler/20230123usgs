
import re

FILE_PATH = "../DATA/mary.txt"

# NOTE: r'\W+' is a regular expression that splits on anything that isn't a letter, number, or underscore

with open(FILE_PATH) as mary_in:
    file_contents = mary_in.read()
    s = {w.lower() for w in re.split(r'\W+', file_contents) if w} # Get unique words from file. Only one line is in memory at a time. Skip "empty" words.
print(s)
