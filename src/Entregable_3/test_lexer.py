import unittest
from lexer import lexer
from parser import parser

data = "TRAEME TODO DE LA TABLA usuarios DONDE edad BETWEEN 18 AND 25;"

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


class TestLexer(unittest.TestCase):

    def test_t_OR(self):
        lexer.input("OR")
        token = lexer.token()
        self.assertEqual(token.type, "OR")
        self.assertEqual(token.value, "OR")

    def test_t_newline(self):
        lexer.input("\n")
        token = lexer.token()
        self.assertIsNone(token)  # No debe retornar tokens para nueva línea

    def test_t_error(self):
        lexer.input("?")
        with self.assertRaises(SyntaxError):
            for token in lexer:
                pass  # Se espera que se produzca una excepción


if __name__ == '__main__':
    unittest.main()
