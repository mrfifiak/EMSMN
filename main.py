import xml.etree.ElementTree as et
import os
from reader import TextReader


reader = TextReader()
data = []
channels = []
programmes = []
for datafile in reader.channel_list:
    data.append(reader.get_programmes(datafile))

for channel_data in data:
    channels.append(channel_data['id'])
    programmes.append(channel_data['programmes'])


print(type(data))
print("\nDEBUG\n")


base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "template.xml")

tree = et.parse(xml_file)

root = tree.getroot()

new_channel = et.SubElement(root, "channel", attrib={"id": "BBC"})
new_prod_ico = et.SubElement(new_channel, "icon", attrib={"src": "ico.png"})

for child in root:
    print(child.tag, child.attrib)