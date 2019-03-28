INTEGER, PLUS, MINUS, MUL, DIV, COMMA, LQ, RQ, LPAREN, \
RPAREN, ID, ASSIGN, BEGIN, END, SEMI, DOT, EOF, STR, IF, ELSE, BOOL = ('INTEGER', 'PLUS', "MINUS", "MUL", "DIV", "COMMA",
                                                        "LQ", "RQ", "LPAREN", "RPAREN", "ID", "ASSIGN",
                                                        "BEGIN", "END", "SEMI", "DOT", "EOF", "STR", "IF", "ELSE", "BOOL")

PRINT, LENGTH, NUM_T, STR_T = 'print', "length", "num", "str"

TRUE, FALSE, EQUAL, LESS, GREAT, LBRANCH, RBRANCH = "TRUE", "FALSE", "EQUAL", "LESS", "GREAT", "LBRANCH", "RBRANCH"
WHILE, FOR = "WHILE", "FOR"


class Token(object):
    def __init__(self, token_type: str, value):
        # this is token type: INTEGER, PLUS or EOF
        self.type = token_type

        # this is token value: 0, ... 9
        self.value = value

    def __str__(self):
        return f"Token<{self.type}><{self.value}>"

    def __repr__(self):
        return self.__str__()
