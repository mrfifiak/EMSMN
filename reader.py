import os
import json


class TextReader:
    def __init__(self, datapath=None):
        if datapath is None:
            self.channel_list = os.listdir("data/")
        else:
            self.channel_list = os.listdir(datapath)

    def get_programmes(self, filename):   # returns list of programmes
        with open("data/" + filename, 'r') as datafile:
            content = datafile.read()
            data = json.loads(content)
        return data
