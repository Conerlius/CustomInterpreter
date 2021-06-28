class Error(object):

    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        res = f'{self.error_name}: {self.details}'
        res += f'{self.pos_start} to {self.pos_end}'


class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, detail):
        super().__init__(pos_start, pos_end, 'Illegal Character', detail)

