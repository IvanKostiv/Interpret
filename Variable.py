from ASTTree import AST
from Token import *


class Variable(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value
