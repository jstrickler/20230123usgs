import lxml.etree as ET

doc = ET.parse('../DATA/solar.xml')  # parse XML file

for planet in doc.findall('.//planet'):  # find all elements (relative to root element) with tag "planet"
    print(planet.get('planetname'))      # get XML attribute value
    for moon in planet.findall('moon'):  # find all child elements with tag "moon"
        print('\t{}'.format(moon.text))  # print text contained in "moon" tag
