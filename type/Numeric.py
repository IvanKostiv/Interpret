from base.ASTTree import AST
from base.Token import *
from type.String import String


class Numeric(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if hasattr(other, 'value'):
            return Numeric(Token(INTEGER, self.value + other.value))
        else:
            return Numeric(Token(INTEGER, self.value + other))

    def __sub__(self, other):
        if hasattr(other, 'value'):
            return Numeric(Token(INTEGER, self.value - other.value))
        else:
            return Numeric(Token(INTEGER, self.value - other))

    def __mul__(self, other):
        if hasattr(other, 'value'):
            return Numeric(Token(INTEGER, self.value * other.value))
        else:
            return Numeric(Token(INTEGER, self.value * other))

    def __truediv__(self, other):
        if hasattr(other, 'value'):
            return Numeric(Token(INTEGER, self.value / other.value))
        else:
            return Numeric(Token(INTEGER, self.value / other))

    def __eq__(self, other):
        if hasattr(other, 'value'):
            return self.value == other.value
        else:
            return self.value == other

    def __lt__(self, other):
        if hasattr(other, "value"):
            return self.value < other.value
        else:
            return self.value < other

    def __gt__(self, other):
        if hasattr(other, 'value'):
            return self.value > other.value
        else:
            return self.value > other

    def __int__(self):
        return int(self.value)

    @staticmethod
    def create_num(num: float):
        return Numeric(Token(INTEGER, num))
