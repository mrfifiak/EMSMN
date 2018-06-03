class TextReader:

    def __init__(self, filename=None):
        self.data = []
        if filename is None:
            self.filename = "data.txt"
        else:
            self.filename = filename

    def read(self):
        with open(self.filename, 'r') as datafile:
            self.data = datafile.read().splitlines()
        for d in self.data:
            print(d)





