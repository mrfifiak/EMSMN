from reader import TextReader
from writer import XMLWriter


reader = TextReader()
writer = XMLWriter()

data = []
channels = []
programmes = []
for datafile in reader.channel_list:
    data.append(reader.get_programmes(datafile))

i = 0
for channel_data in data:
    channels.append(channel_data['id'])
    for p in channel_data['programmes']:
        p['channel'] = channel_data['id']
        programmes.append(p)

writer.add_channels(channels)
writer.add_programmes(programmes)
print(type(data))
print("\nDEBUG\n")

writer.save()
