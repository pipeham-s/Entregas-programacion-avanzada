from lexer import lexer
from parser import parser

data = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
