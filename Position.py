class Position(object):
    def __init__(self, idx, ln, col, fn, txt):
        self.index = idx
        self.line = ln
        self.col = col
        self.file_name = fn
        self.content = txt

    def advance(self, current_char):
        self.index += 1
        self.col += 1

        if current_char =='\n':
            self.col = 0

    def copy(self):
        return Position(self.index, self.line, self.col, self.file_name, self.content)
