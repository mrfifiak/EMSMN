class TextReader:

    def __init__(self, filename=None):
        if filename is None:
            self.filename = "data.txt"
        else:
            self.filename = filename

    def read(self):
        with open(self.filename, 'r') as datafile:
            data = datafile.read().splitlines()
        for d in data:
            print(d)
        return data





