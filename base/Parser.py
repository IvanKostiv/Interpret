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
        # else:
        #     node = self.variable()
        #     return node

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

    def expr(self):
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token

            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinaryOperation(left=node, operation=token, right=self.term())

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

        elif self.current_token.type == PRINT:
            self.eat(PRINT)

            # if self.current_token.type == STR:
            #     node = Print(self.str())
            # else:
            #     node = Print(self.expr())
            node = Print(self.expr())

        else:
            node = self.empty()

        return node

    def assignment_statement(self):
        left = self.variable()

        token = self.current_token
        self.eat(ASSIGN)

        # if self.current_token.type == STR:
        #     right = self.str()
        #
        # elif self.current_token.type == LQ:
        #     right = self.list()
        # else:
        right = self.expr()

        node = Assign(left, token, right)

        return node

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
            arg_list.append(self.current_token)
            self.eat(self.current_token.type)

        self.eat(RPAREN)

        return MethodCall(variable, method, arg_list)

    def empty(self):
        return NoOperation()

    def parse(self):
        node = self.program()

        if self.current_token.type != EOF:
            self.error()

        return node
