class TextReader:

    def __init__(self, filename=None):
        self.data = []
        if filename is None:
            self.filename = "data.txt"
        else:
            self.filename = filename



