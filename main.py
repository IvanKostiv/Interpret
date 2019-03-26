from base.Interpreter import *


def main():
    while True:
        try:
            text = input("calc>>> ")

        except EOFError:
            break

        if not text:
            continue

        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()

        print(interpreter.GLOBAL_SCOPE)

        if result is not None:
            print(result)
        # file = open("main.lan")
        # lines = "".join(file.readlines())
        #
        # lexer = Lexer(lines)
        # parser = Parser(lexer)
        # interpreter = Interpreter(parser)
        # result = interpreter.interpret()
        # print(interpreter.GLOBAL_SCOPE)


if __name__ == '__main__':
    main()
