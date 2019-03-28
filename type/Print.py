from base.ASTTree import AST
from type.List import List


class Print(AST):
    def __init__(self, token):
        self.print = token

    def print_list(self, node):
        result = "["

        for item in node.value[:-1]:
            if type(item) == List:
                result += self.print_list(item)
            else:
                result += str(item.value) + ", "
        result += str(node.value[-1].value)
        result += ']'
        return result


class Length(AST):
    def __init__(self, node):
        self.node = node


class StrT(AST):
    def __init__(self, node):
        self.node = node


class NumT(AST):
    def __init__(self, node):
        self.node = node
