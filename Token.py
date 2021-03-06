class Token(object):
    def __init__(self, type_, value_=None):
        self.type = type_
        self.value = value_

    def __repr__(self):
        if self.value:
            return f'{self.type} : {self.value}'
        return f'{self.type}'
