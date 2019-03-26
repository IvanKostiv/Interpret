from base.ASTTree import AST
from type.List import List


class Print(AST):
    def __init__(self, token):
        self.print = token

    def print_list(self, node):
        result = "["

        for item in node.value:
            if type(item) == List:
                result += self.print_list(item)
            else:
                result += str(item.value) + ", "

        result += ']'
        return result
