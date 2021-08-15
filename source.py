class Source:
    def __init__(self, src, line, offset):
        self.src = src
        self.line = line
        self.offset = offset

    def __eq__(self, other):
        if self.src == other.src and self.line == other.line:
            return True
        return False

    def __gt__(self, other):
        if self.src > other.src:
            return True
        if self.src == other.src and self.line > other.line:
            return True
        if self.src == other.src and self.line > other.line and self.offset > other.offset:
            return True
        return False

    def __lt__(self, other):
        if self.src < other.src:
            return True
        if self.src == other.src and self.line < other.line:
            return True
        if self.src == other.src and self.line < other.line and self.offset < other.offset:
            return True
        return False
