import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()
# root = ET.fromstring(country_data_as_string)

for child in root:
    print child.tag, child.attrib

for neighbor in root.iter('neighbor'):
    print neighbor.attrib

for country in root.findall('country'):
    rank = country.find('rank').text
    year = country.find('year').text
    name = country.get('name')  # attrib only
    print name, year, rank

for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')

for item in root.findall('country'):
    name = item.get('name')

    if (name == 'Liechtenstein'):
        pop = ET.SubElement(item, "population")
        pop.text = "1234"
        pop.tail = "\n"

    if (name == 'Singapore'):
        pop = ET.Element("population")
        pop.text = "3456"
        pop.tail = "\n"
        item.append(pop)

tree.write('country_data_1.xml')
