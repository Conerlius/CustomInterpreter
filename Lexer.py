from Position import Position


class Lexer(object):
    def __init__(self, fn, txt):
        self.fn = fn
        self.text = txt
        self.pos = Position(-1, 0, -1, fn, txt)
        self.current_char = None
        self.advance()

    def advance(self):
        pass

    def make_tokens(self):
        tokens = []
        '''
        遍历text
        遍历中，分别判断获取的内容
        '''