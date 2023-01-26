import lxml.etree as et

doc = et.parse('DATA/solar.xml')
print(f"doc: {doc}")

root = doc.getroot()

print(f"root: {root}")
print(f"root.tag: {root.tag}")

for child in root:
    if 'planets' in child.tag:
        for planet in child:
            print(planet.get('planetname'))
            for moon in planet:
                print(f"   {moon.text}")

print('-' * 60)

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet:
        print(f"   {moon.text}")





