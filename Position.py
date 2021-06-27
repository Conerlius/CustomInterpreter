class Position(object):
    def __init__(self, idx, ln, col, fn, txt):
        self.index = idx
        self.line = ln
        self.col = col
        self.file_name = fn
        self.content = txt
