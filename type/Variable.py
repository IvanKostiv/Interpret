from base.ASTTree import AST
from base.Token import *


class Variable(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value
