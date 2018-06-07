import xml.etree.ElementTree as xml
import sys

txtFile = sys.argv[1]
xmlFile = sys.argv[1]

root = xml.Element("Users")
root.text = "\n\t"
root.set('version', '1.0')
root.set('language', 'EN')
userElement = xml.Element("user")
userElement.text = "\n\t\t"

uid = xml.SubElement(userElement, "uid")
uid.text = "1"
uid.tail = "\n\t\t"
FirstName = xml.SubElement(userElement, "FirstName")
FirstName.text = "testuser"
FirstName.tail = "\n\t\t"
LastName = xml.SubElement(userElement, "LastName")
LastName.text = "testuser"
LastName.tail = "\n\t\t"
Email = xml.SubElement(userElement, "Email")
Email.text = "testuser@test.com"
Email.tail = "\n\t\t"
state = xml.SubElement(userElement, "state")
state.text = "xyz"
state.tail = "\n\t\t"
location = xml.SubElement(userElement, "location")
location.text = "abc"
location.tail = "\n\t"

userElement.tail = "\n"
root.append(userElement)

tree = xml.ElementTree(root)
with open(xmlFile, "w") as fh:
    tree.write(fh, encoding='utf-8', xml_declaration=True)

tree = xml.parse(xmlFile)
root = tree.getroot()
tag = root.tag
attrib = root.attrib
children = root.getchildren()

xml.dump(root)
print tag
print attrib
print children
