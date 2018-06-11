from lxml import etree as et


class XMLWriter:
    def __init__(self, output_name=None):
        if output_name is None:
            self.output_name = "epg.xml"
        else:
            self.output_name = output_name
        with open(self.output_name, 'w+') as out_file:
            out_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?><tv generator-info-name=\"EMSMN Project XMLTV Generator\"></tv>")
        self.tree = et.parse(self.output_name)
        self.root = self.tree.getroot()

    def add_channels(self, channels):
        for ch in channels:
            new_channel = et.SubElement(self.root, "channel", attrib={"id": ch})

    def add_programmes(self, programmes):
        for p in programmes:
            new_programme = et.SubElement(self.root, "programme", attrib={"start": p['start'], "stop": p['stop'], "channel": p['channel']})
            new_title = et.SubElement(new_programme, "title", attrib={"lang": "en"})
            new_title.text = p['title']
            new_desc = et.SubElement(new_programme, "desc", attrib={"lang": "en"})
            new_desc.text = p['desc']
            new_category = et.SubElement(new_programme, "category", attrib={"lang": "en"})
            new_category.text = p['category']
            if 'episode-num' in p.keys():
                new_ep_num = et.SubElement(new_programme, "episode-num")
                new_ep_num.text = str(p['episode-num'])

    def save(self):
        self.tree.write(self.output_name, pretty_print=True)


