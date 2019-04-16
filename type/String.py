from base.ASTTree import *


class String(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value: str = token.value

    def at(self, pos: int):
        if pos > len(self.value) - 1:
            raise Exception("out of range")
        else:
            return String(Token("STR", self.value[int(pos)]))

    def substring(self, start: int, end: int):
        if (start > len(self.value) - 1) and start < 0:
            raise Exception("Out of range")
        elif (end > len(self.value) - 1) and end < 0:
            raise Exception("Out of range")
        else:
            return String(Token("STR", self.value[int(start):int(end)]))

    def __add__(self, other):
        if type(other.value) in (float, int):
            return String(Token("STR", self.value + str(other.value)))
        else:
            return String(Token("STR", self.value + other.value))

    def __mul__(self, other):
        return String(Token("STR", self.value * int(other.value)))

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __float__(self):
        return float(self.value)

    @staticmethod
    def create_string(string: str):
        return String(Token(STR, string))
