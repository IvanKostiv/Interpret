from ASTTree import *
from Variable import Variable


class Assign(AST):
    def __init__(self, left_token: Variable, operation: Token, right_token: Token):
        self.left = left_token
        self.operation = operation
        self.right = right_token
