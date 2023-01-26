from dataclasses import dataclass

@dataclass
class President:
    first_name: str
    last_name: str
    birth_state: str

p = President('George', 'Washington', 'Virginia')
print(p.last_name)
