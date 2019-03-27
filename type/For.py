from base.ASTTree import AST


class For(AST):
    def __init__(self, condition, assignment, body, change_node):
        self.condition = condition
        self.assignment = assignment
        self.body = body
        self.change_node = change_node
