from base.ASTTree import *


class While(AST):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
