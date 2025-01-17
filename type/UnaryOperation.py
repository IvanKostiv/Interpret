from base.Token import *
from base.ASTTree import AST


class UnaryOperation(AST):
    def __init__(self, operation: Token, expr):
        self.operation = operation
        self.expr = expr
