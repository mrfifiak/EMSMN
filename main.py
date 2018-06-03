import xml.etree.ElementTree as et
import os
from reader import TextReader
from writer import XMLWriter


reader = TextReader()
writer = XMLWriter()

data = []
channels = []
programmes = []
for datafile in reader.channel_list:
    data.append(reader.get_programmes(datafile))

for channel_data in data:
    channels.append(channel_data['id'])
    programmes.append(channel_data['programmes'])

writer.add_channels(channels)
print(type(data))
print("\nDEBUG\n")


tree = et.parse("template.xml")

root = tree.getroot()

new_channel = et.SubElement(root, "channel", attrib={"id": "BBC"})
new_prod_ico = et.SubElement(new_channel, "icon", attrib={"src": "ico.png"})

for child in root:
    print(child.tag, child.attrib)
print("\nCHECK\n")
writer.save()
