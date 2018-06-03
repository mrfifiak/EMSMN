import xml.etree.ElementTree as et


class XMLWriter:
    def __init__(self, output_name=None):
        if output_name is None:
            self.output_name = "epg.xml"
        else:
            self.output_name = output_name
        with open("output/" + self.output_name, 'w') as out_file:
            out_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<tv generator-info-name=\"EMSMN Project XMLTV Generator\">\n</tv>")
        self.tree = et.parse("output/" + self.output_name)
        self.root = self.tree.getroot()

    def add_channels(self, channels):
        for ch in channels:
            new_channel = et.SubElement(self.root, "channel", attrib={"id": ch})
            print(new_channel.tag, new_channel.attrib)

    def save(self):
        for child in self.root:
            print(child.tag, child.attrib)
        self.tree.write("output/" + self.output_name)


