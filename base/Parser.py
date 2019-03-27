from base.Lexer import *
from base.Token import *
from type.Numeric import Numeric
from type.BinOperation import BinaryOperation
from type.UnaryOperation import UnaryOperation
from type.Compound import Compound
from type.NoOperation import NoOperation
from type.Assign import Assign
from type.Variable import Variable
from type.Print import Print
from type.String import String
from type.List import List
from type.MethodCall import MethodCall
from type.If import If
from type.While import While
from type.For import For


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer

        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token

        if token.type == INTEGER:
            self.eat(INTEGER)
            return Numeric(token)

        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

        elif token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOperation(token, self.factor())
            return node
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOperation(token, self.factor())
            return node

        elif token.type == STR:
            node = self.str()
            return node

        elif token.type == LQ:
            node = self.list()
            return node
        elif token.type == ID:
            if self.lexer.get_next_token_without_change_pos().type == DOT:
                node = self.method()
                return node
            else:
                node = self.variable()
                return node

    def term(self):
        node = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token

            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)

            node = BinaryOperation(left=node, operation=token, right=self.factor())

        return node

    def cond(self):
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token

            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinaryOperation(left=node, operation=token, right=self.term())

        return node

    def expr(self):
        node = self.cond()

        while self.current_token.type in (EQUAL, GREAT, LESS):
            token = self.current_token

            if token.type == EQUAL:
                self.eat(EQUAL)
            elif token.type == GREAT:
                self.eat(GREAT)
            elif token.type == LESS:
                self.eat(LESS)

            node = BinaryOperation(left=node, operation=token, right=self.cond())

        return node

    def program(self):
        node = self.compound_statement()
        # self.eat(DOT)

        return node

    def compound_statement(self):
        # self.eat(BEGIN)

        nodes = self.statement_list()
        # self.eat(END)

        root = Compound()

        for node in nodes:
            root.children.append(node)

        return root

    def statement_list(self):
        node = self.statement()

        results = [node]

        while self.current_token.type == SEMI:
            self.eat(SEMI)
            results.append(self.statement())

        if self.current_token.type == ID:
            self.error()

        return results

    def statement(self):
        if self.current_token.type == BEGIN:
            node = self.compound_statement()
        elif self.current_token.type == ID:
            if self.lexer.get_next_token_without_change_pos().type == DOT:
                node = self.method()
            else:
                node = self.assignment_statement()
        elif self.current_token.type == IF:
            node = self.condition_statement()

        elif self.current_token.type in (WHILE, FOR):
            node = self.cycle_statement()

        elif self.current_token.type == PRINT:
            self.eat(PRINT)
            node = Print(self.expr())

        else:
            node = self.empty()

        return node

    def assignment_statement(self):
        left = self.variable()

        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()

        node = Assign(left, token, right)

        return node

    def condition_statement(self):
        self.eat(IF)

        self.eat(LPAREN)
        condition = self.expr()
        self.eat(RPAREN)

        self.eat(LBRANCH)
        body = self.compound_statement()
        self.eat(RBRANCH)
        else_body = None

        if self.current_token.type == ELSE:
            self.eat(ELSE)
            self.eat(LBRANCH)

            else_body = self.compound_statement()

            self.eat(RBRANCH)

        return If(body, condition, else_body)

    def cycle_statement(self):

        if self.current_token.type == WHILE:
            self.eat(WHILE)

            self.eat(LPAREN)
            condition = self.expr()
            self.eat(RPAREN)

            self.eat(LBRANCH)
            body = self.compound_statement()
            self.eat(RBRANCH)

            return While(condition, body)
        elif self.current_token.type == FOR:
            self.eat(FOR)

            self.eat(LPAREN)
            assignment = self.assignment_statement()
            self.eat(SEMI)

            condition = self.expr()
            self.eat(SEMI)

            change_node = self.assignment_statement()
            self.eat(RPAREN)

            self.eat(LBRANCH)
            body = self.compound_statement()
            self.eat(RBRANCH)

            return For(condition, assignment, body, change_node)

    def item(self):
        token = self.current_token
        if token.type == STR:
            node = self.str()
        else:
            node = self.expr()

        return node

    def list(self):
        self.eat(LQ)
        node = self.item()

        result = [node]

        while self.current_token.type == COMMA:
            self.eat(COMMA)
            result.append(self.item())

        self.eat(RQ)

        return List(result)

    def variable(self):
        node = Variable(self.current_token)
        self.eat(ID)

        return node

    def str(self):
        node = self.current_token
        self.eat(STR)

        return String(node)

    def method(self):
        # TODO method call
        variable = self.variable()
        self.eat(DOT)

        arg_list = []

        method = self.variable()
        self.eat(LPAREN)

        while self.current_token.type != RPAREN:
            arg_list.append(self.expr())

            if self.current_token.type == COMMA:
                self.eat(COMMA)

        self.eat(RPAREN)

        return MethodCall(variable, method, arg_list)

    def empty(self):
        return NoOperation()

    def parse(self):
        node = self.program()

        if self.current_token.type != EOF:
            self.error()

        return node
