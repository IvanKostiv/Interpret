from ASTTree import AST


class Print(AST):
    def __init__(self, token):
        self.print = token
