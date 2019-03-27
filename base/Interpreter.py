from base.Parser import *
from base.NodeVisitor import NodeVisitor
from type.BinOperation import BinaryOperation
from type.Numeric import Numeric
from type.UnaryOperation import UnaryOperation
from type.Compound import Compound
from type.Variable import Variable
from type.Assign import Assign
from type.NoOperation import NoOperation
from type.Print import Print


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

        elif node.operation.type == EQUAL:
            return self.visit(node.left) == self.visit(node.right)

        elif node.operation.type == LESS:
            return self.visit(node.left) < self.visit(node.right)

        elif node.operation.type == GREAT:
            return self.visit(node.left) > self.visit(node.right)

    def visit_Numeric(self, node: Numeric):
        return node.value

    def visit_String(self, node: String):
        return node

    def visit_UnaryOperation(self, node: UnaryOperation):
        operation = node.operation.type

        if operation == PLUS:
            return +self.visit(node.expr)
        elif operation == MINUS:
            return -self.visit(node.expr)

    def visit_Compound(self, node: Compound):
        for child in node.children:
            self.visit(child)

    def visit_Token(self, node: Token):
        return node.value

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
        print_info = self.visit(node.print)

        if type(print_info) == List:
            result = "["
            for item in print_info.value:
                print_a = self.visit(item)
                if hasattr(print_a, "value"):
                    result += str(print_a.value) + ", "
                else:
                    result += str(print_a) + ", "

            print(result + "]")
        else:
            if hasattr(print_info, "value"):
                print(print_info.value)
            else:
                print(print_info)

    def visit_List(self, node: List):
        return node

    def visit_MethodCall(self, node: MethodCall):
        variable = node.variable_name
        method = node.method_name

        called_method = getattr(self.visit(variable), method)

        arg_list = []

        for arg in node.arg:
            arg_list.append(self.visit(arg))

        return called_method(*arg_list)

    def visit_If(self, node: If):
        result_condition = self.visit(node.condition)

        if bool(result_condition):
            self.visit(node.body)
        elif node.else_body is not None:
            self.visit(node.else_body)
        else:
            pass

    def visit_While(self, node: While):
        while bool(self.visit(node.condition)):
            self.visit(node.body)

    def visit_For(self, node: For):
        self.visit(node.assignment)

        while bool(self.visit(node.condition)):
            self.visit(node.body)
            self.visit(node.change_node)

    def visit_NoOperation(self, node: NoOperation):
        pass

    def interpret(self):
        tree = self.parser.parse()

        if tree is None:
            return ""

        return self.visit(tree)
