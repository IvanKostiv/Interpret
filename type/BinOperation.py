from base.ASTTree import AST
from base.Token import Token


class BinaryOperation(AST):
    def __init__(self, left: Token, operation: Token, right: Token):
        self.left = left
        self.token = self.operation = operation
        self.right = right
