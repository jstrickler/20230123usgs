
fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']

values = [2, 42, 18, 92, "boom", ['a', 'b', 'c']]

ufruits = [fruit.upper() for fruit in fruits]  # Copy each fruit to upper case

afruits = [fruit for fruit in fruits if fruit.startswith('a')]  # Select each fruit if it starts with 'a'

doubles = [v * 2 for v in values]  # Copy each number, doubling it

print("ufruits:", " ".join(ufruits))
print("afruits:", " ".join(afruits))
print("doubles:", end=' ')
for d in doubles:
    print(d, end=' ')
print()
