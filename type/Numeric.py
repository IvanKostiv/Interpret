from base.ASTTree import AST
from base.Token import Token


class Numeric(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value


    def printlol(self):
        print("Lol");