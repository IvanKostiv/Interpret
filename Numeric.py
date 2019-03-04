from ASTTree import AST
from Token import Token


class Numeric(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value
