from base.ASTTree import *


class String(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def at(self, pos: int):
        if pos > len(self.value) - 1:
            raise Exception("out of range")
        else:
            return String(Token("STR", self.value[int(pos)]))

    def printF(self):
        print("F")

    def __add__(self, other):
        return String(Token("STR", self.value + other.value))
