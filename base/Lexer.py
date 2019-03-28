from base.Token import *

REVERSED_KEYWORDS = {
    "BEGIN": Token('BEGIN', 'BEGIN'),
    "END": Token('END', 'END'),
    "True": Token('TRUE', "TRUE"),
    "False": Token('FALSE', "FALSE"),
    'if': Token('IF', "IF"),
    'else': Token('ELSE', "ELSE"),
    'while': Token("WHILE", "WHILE"),
    'for': Token("FOR", "FOR")
}

REVERSED_FUNCTION = [PRINT, LENGTH, NUM_T, STR_T]


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0

        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Invalid character")

    def peek(self):
        peek_pos = self.pos
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def peek_next(self):
        peek_pos = self.pos + 1

        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def find_expression(self):
        result = ''
        self.advance()

        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '') and self.current_char != ')':
            result += self.current_char
            self.advance()
        self.advance()

        return result

    def _id(self):
        result = ""
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()

        if result in REVERSED_FUNCTION:
            token = Token(result, str(result))
            return token
        # elif self.peek() == '.':
        #     pass
        else:
            token = REVERSED_KEYWORDS.get(result, Token(ID, result))  # return ID token, if name is not reversed keywords
            return token

    def advance(self):
        """advance the pos pointer and set the current_char variable"""
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''

        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return float(result)

    def str(self):
        result = ''

        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()

        self.advance()

        return result

    def find_list(self):
        result = ''

        while self.current_char is not None and self.current_char != ']':
            result += self.current_char
            self.advance()

        self.advance()
        return result

    def get_next_token(self):

        """
        LEXER FOR INTERPRETER
        :return: TOKENS
        """

        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            elif self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            elif self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            elif self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            elif self.current_char == '+':
                self.advance()
                return Token(PLUS, "+")

            elif self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            elif self.current_char == '(':
                self.advance()
                return Token(LPAREN, "(")

            elif self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            elif self.current_char == '=':
                if self.peek_next() == '=':
                    self.advance()
                    self.advance()
                    return Token(EQUAL, '==')
                else:
                    self.advance()
                    return Token(ASSIGN, '=')

            elif self.current_char == ';':
                self.advance()
                return Token(SEMI, ';')

            elif self.current_char == '.':
                self.advance()
                return Token(DOT, '.')

            elif self.current_char.isalpha():
                return self._id()

            elif self.current_char == '[':
                self.advance()
                return Token(LQ, "[")

            elif self.current_char == ']':
                self.advance()
                return Token(RQ, "]")

            elif self.current_char == ',':
                self.advance()
                return Token(COMMA, ',')

            elif self.current_char == '"':
                self.advance()
                return Token(STR, self.str())

            elif self.current_char == '>':
                self.advance()
                return Token(GREAT, '>')
            elif self.current_char == '<':
                self.advance()
                return Token(LESS, '<')

            elif self.current_char == '{':
                self.advance()
                return Token(LBRANCH, '{')

            elif self.current_char == '}':
                self.advance()
                return Token(RBRANCH, '}')

            self.error()
        return Token(EOF, None)

    def get_next_token_without_change_pos(self):
        current_pos = self.pos
        current_char = self.current_char
        token = self.get_next_token()

        self.pos = current_pos
        self.current_char = current_char
        return token
