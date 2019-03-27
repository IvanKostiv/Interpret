from base.ASTTree import *


class If(AST):
    def __init__(self, body, condition, else_body=None):
        self.body = body
        self.condition = condition
        self.else_body = else_body
