from base.ASTTree import *
from type.Variable import Variable


class MethodCall(AST):
    def __init__(self, variable: Variable, method: Variable, arg: list = None):
        self.variable_name = variable
        self.method_name = method.value
        self.arg_token = arg
        self.arg_value = []

        for token in self.arg_token:
            if token.type != COMMA:
                self.arg_value.append(token.value)
