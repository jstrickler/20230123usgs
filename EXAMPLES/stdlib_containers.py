from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter
with open('../DATA/words.txt') as words_in:
    all_words = [line[0] for line in words_in]
    word_counter = Counter(all_words)  # Count list of words by passing iterable of words to Counter instance


print(word_counter.most_common(10))  # Counter.most_common() return n most common occurrences
print('-' * 60)

# defaultdict
fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]

fruit_by_first = defaultdict(list)  # Create default dict whose default value is a new list object

for fruit in fruits:
    fruit_by_first[fruit[0]].append(fruit)  # Append fruit to dictionary element whose key is the first letter and whose value is a list

for letter, fruits in sorted(fruit_by_first.items()):
    print(letter, fruits)
print('-' * 60)

# deque
d = deque()  # Create an empty deque
for c in 'abcdef':
    d.append(c)   # Append to the deque
print(d)
for c in 'ghijkl':
    d.appendleft(c)  # Prepend to the deque
print(d)
d.extend('mno')  # Extend the deque at the end one letter at a time
print(d)
d.extendleft('pqr')  # Extend the deque at the beginning one letter at a time
print(d)
print(d[9])
print(d.pop(), d.popleft())  # Pop from end, beginning
print(d)
print('-' * 60)


# namedtuple
President = namedtuple('President', 'first_name, last_name, party')  # Create named tuple with specified fields
p = President('Theodore', 'Roosevelt', 'Republican')  # Create instance of named tuple
print(p, len(p))
print(p[0], p[1], p[-1])
print(p.first_name, p.last_name, p.party)  # Access tuple fields by name

p = President(last_name='Lincoln', party='Republican', first_name='Abraham')
print(p)
print(p.first_name, p.last_name)
print('-' * 60)

