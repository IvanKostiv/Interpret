from base.ASTTree import *


class Import(AST):
    def __init__(self, file_name):
        self.file_name = file_name
