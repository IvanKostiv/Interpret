from base.ASTTree import *


class Bool(AST):
    def __init__(self, token: Token):
        self.value = token.value
