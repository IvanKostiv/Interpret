from ASTTree import *


class String(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value
