from base.ASTTree import *


class List(AST):
    def __init__(self, _list: list):
        self.value = _list

    def __str__(self):
        result_string = ""
        for item in self.value:
            result_string += str(item.value) + ", "

        return result_string