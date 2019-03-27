from base.ASTTree import *
from type.Variable import Variable


class MethodCall(AST):
    def __init__(self, variable: Variable, method: Variable, arg: list = None):
        self.variable_name = variable
        self.method_name = method.value
        self.arg = arg
