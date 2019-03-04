from Parser import *
from NodeVisitor import NodeVisitor
from BinOperation import BinaryOperation
from Numeric import Numeric
from UnaryOperation import UnaryOperation
from Compound import Compound
from Variable import Variable
from Assign import Assign
from NoOperation import NoOperation
# from Token import *
from Print import Print


class Interpreter(NodeVisitor):

    GLOBAL_SCOPE = {}

    def __init__(self, parser: Parser):
        self.parser = parser

    def visit_BinaryOperation(self, node: BinaryOperation):
        if node.operation.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)

        elif node.operation.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)

        elif node.operation.type == MUL:
            return self.visit(node.left) * self.visit(node.right)

        elif node.operation.type == DIV:
            return self.visit(node.left) / self.visit(node.right)

    def visit_Numeric(self, node: Numeric):
        return node.value

    def visit_UnaryOperation(self, node: UnaryOperation):
        operation = node.operation.type

        if operation == PLUS:
            return +self.visit(node.expr)
        elif operation == MINUS:
            return -self.visit(node.expr)

    def visit_Compound(self, node: Compound):
        for child in node.children:
            self.visit(child)

    def visit_Assign(self, node: Assign):
        var_name = node.left.value
        self.GLOBAL_SCOPE[var_name] = self.visit(node.right)

    def visit_Variable(self, node: Variable):
        var_name = node.value

        value = self.GLOBAL_SCOPE.get(var_name)

        if value is None:
            raise NameError(repr(var_name))
        else:
            return value

    def visit_Print(self, node: Print):
        print(self.visit(node.print))

    def visit_NoOperation(self, node: NoOperation):
        pass

    def interpret(self):
        tree = self.parser.parse()

        if tree is None:
            return ""

        return self.visit(tree)
