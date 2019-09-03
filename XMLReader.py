import xml.etree.ElementTree as ET

tree = ET.parse("sample.xml")
root = tree.getroot()

for table in root.findall('./home/table/'):
    for desk in table:
        if "{www.w3c.org/xml}" in desk.tag:
            print(desk.tag,desk.text)
        else:
            print("Deprecated--> %s : %s"%(desk.tag,desk.text))
