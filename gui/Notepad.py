from tkinter import *
import tkinter.scrolledtext as sclt
from base.Interpreter import *


def run():
    console_area.configure(state='normal')
    console_area.delete("1.0", 'end-1c')
    console_area.configure(state='disabled')

    text = code_area.get("1.0", 'end-1c')
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)

    interpreter.interpret()

    console_area_text = open('output.txt', 'r+')

    result_string = ""

    for line in console_area_text.readlines():
        result_string += line

    console_area_text.close()

    console_area_text = open('output.txt', 'w')
    console_area_text.write("")
    console_area_text.close()

    console_area.configure(state='normal')
    console_area.insert(INSERT, result_string)
    console_area.configure(state='disabled')


root = Tk()
root.geometry("640x480")
root.title("Interpreter")

code_area = sclt.ScrolledText(root, wrap=WORD)
console_area = sclt.ScrolledText(root, wrap=WORD, state='disabled')
run_button = Button(root, text='run', font='Arial 14')

run_button.bind("<Button-1>", lambda event: run())

code_area.pack(side='top', expand=1, fill=X)
run_button.pack(side='bottom', expand=1, fill=X)
console_area.pack(side='bottom', expand=1, fill=X)

root.mainloop()
