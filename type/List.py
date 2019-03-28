from base.ASTTree import *


class List(AST):
    def __init__(self, _list: list):
        self.value = _list
        self.len_value = len(_list)

    def __str__(self):
        result_string = ""
        for item in self.value:
            result_string += str(item.value) + ", "

        return result_string

    def __len__(self):
        return len(self.value)

    def at(self, pos):
        if pos > len(self.value) - 1:
            raise Exception("Out of range")
        else:
            return self.value[int(pos)]
