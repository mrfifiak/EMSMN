import os
import json


class TextReader:
    def __init__(self):
        self.filelist = os.listdir("data/")

    def read(self):
        with open("data/BBC.json", 'r') as datafile:
            content = datafile.read()
            data = json.loads(content)
            print(type(data))
        return data
