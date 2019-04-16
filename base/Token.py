INTEGER, PLUS, MINUS, MUL, DIV, COMMA, LQ, RQ, LPAREN, \
RPAREN, ID, ASSIGN, BEGIN, END, SEMI, DOT, EOF, STR, IF, ELSE, BOOL = ('INTEGER', 'PLUS', "MINUS", "MUL", "DIV", "COMMA",
                                                        "LQ", "RQ", "LPAREN", "RPAREN", "ID", "ASSIGN",
                                                        "BEGIN", "END", "SEMI", "DOT", "EOF", "STR", "IF", "ELSE", "BOOL")

PRINT, LENGTH, NUM_T, STR_T = 'print', "length", "num", "str"

TRUE, FALSE, EQUAL, LESS, GREAT, LBRANCH, RBRANCH = "TRUE", "FALSE", "EQUAL", "LESS", "GREAT", "LBRANCH", "RBRANCH"
WHILE, FOR = "WHILE", "FOR"

THREAD = "THREAD"


class Token(object):
    def __init__(self, token_type: str, value):
        self.type = token_type
        self.value = value

    def __str__(self):
        return f"Token<{self.type}><{self.value}>"

    def __repr__(self):
        return self.__str__()
