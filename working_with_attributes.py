from president import President

p = President(1)
print(p.first_name, p.last_name)

print(f"p: {p}")
print(f"dir(p): {dir(p)}")
print()

field_name = "party"
print(f"getattr(p, field_name): {getattr(p, field_name)}")
print(f"getattr(p, 'birth_place'): {getattr(p, 'birth_place')}")

fields = 'party', 'birth_place', 'birth_state', 'alcohol capacity'

for field in fields:
    if hasattr(p, field):
        print(f"{field}: {getattr(p, field)}")

print(f"getattr(p, 'wombat', None): {getattr(p, 'wombat', None)}")
print(f"getattr(p, 'wombat', 'NOT FOUND'): {getattr(p, 'wombat', 'NOT FOUND')}")

def bark(self):
    print("woof! woof!")

setattr(President, "bark", bark)

p.bark()

delattr(President, "bark")

p.bark()