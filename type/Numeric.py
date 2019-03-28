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
        return Numeric(Token(INTEGER, self.value + other.value))

    def __sub__(self, other):
        return Numeric(Token(INTEGER, self.value - other.value))

    def __mul__(self, other):
        return Numeric(Token(INTEGER, self.value * other.value))

    def __truediv__(self, other):
        return Numeric(Token(INTEGER, self.value / other.value))

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    @staticmethod
    def create_num(num: float):
        return Numeric(Token(INTEGER, num))
