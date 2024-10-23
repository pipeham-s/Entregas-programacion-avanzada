import ply.lex as lex

# Lista de tokens
tokens = [
    # Palabras clave SQL
    'SELECT', 'FROM', 'WHERE', 'DISTINCT', 'INSERT_INTO', 'VALUES',
    'UPDATE', 'SET', 'DELETE_FROM', 'JOIN', 'ON', 'GROUP_BY', 'HAVING',
    'ALTER_TABLE', 'ADD_COLUMN', 'DROP_COLUMN', 'BETWEEN', 'AND', 'NOT_NULL', 'COUNT',

    # Palabras clave USQL
    'TRAEME', 'DE_LA_TABLA', 'DONDE', 'LOS_DISTINTOS', 'METE_EN', 'LOS_VALORES',
    'ACTUALIZA', 'SETEA', 'BORRA_DE_LA', 'MEZCLANDO', 'EN', 'AGRUPANDO_POR',
    'WHERE_DEL_GROUP_BY', 'CAMBIA_LA_TABLA', 'AGREGA_LA_COLUMNA', 'ELIMINA_LA_COLUMNA',
    'ENTRE', 'Y', 'NO_NULO', 'CONTANDO', 'TODO',

    # Símbolos y operadores
    'ASTERISK', 'COMMA', 'SEMICOLON', 'LPAREN', 'RPAREN', 'EQUALS', 'GREATER_THAN', 'LESS_THAN', 'GE', 'LE', 'NE', 'DOT', 'OR',

    # Identificadores y literales
    'IDENTIFIER', 'STRING', 'NUMBER',
]

# Ignorar espacios y tabs
t_ignore = ' \t'

# Operadores y símbolos
t_ASTERISK = r'\*'


t_COMMA = r','
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GE = r'>='
t_LE = r'<='
t_NE = r'<>|!='
t_DOT = r'\.'


t_OR = r'OR'

# Palabras clave de SQL y USQL y su mapeo a tokens


def t_SELECT(t):
    r'SELECT'
    return t


def t_FROM(t):
    r'FROM'
    return t


def t_WHERE(t):
    r'WHERE'
    return t


def t_DISTINCT(t):
    r'DISTINCT'
    return t


def t_INSERT_INTO(t):
    r'INSERT\s+INTO'
    return t


def t_VALUES(t):
    r'VALUES'
    return t


def t_UPDATE(t):
    r'UPDATE'
    return t


def t_SET(t):
    r'SET'
    return t


def t_DELETE_FROM(t):
    r'DELETE\s+FROM'
    return t


def t_JOIN(t):
    r'JOIN'
    return t


def t_ON(t):
    r'ON'
    return t


def t_GROUP_BY(t):
    r'GROUP\s+BY'
    return t


def t_HAVING(t):
    r'HAVING'
    return t


def t_ALTER_TABLE(t):
    r'ALTER\s+TABLE'
    return t


def t_ADD_COLUMN(t):
    r'ADD\s+COLUMN'
    return t


def t_DROP_COLUMN(t):
    r'DROP\s+COLUMN'
    return t


def t_BETWEEN(t):
    r'BETWEEN'
    return t


def t_AND(t):
    r'AND'
    return t


def t_NOT_NULL(t):
    r'NOT\s+NULL'
    return t


def t_COUNT(t):
    r'COUNT'
    return t

# Definir las palabras clave de USQL


def t_TRAEME(t):
    r'TRAEME'
    return t


def t_DE_LA_TABLA(t):
    r'DE\s+LA\s+TABLA'
    return t


def t_DONDE(t):
    r'DONDE'
    return t


def t_LOS_DISTINTOS(t):
    r'LOS\s+DISTINTOS'
    return t


def t_METE_EN(t):
    r'METE\s+EN'
    return t


def t_LOS_VALORES(t):
    r'LOS\s+VALORES'
    return t


def t_ACTUALIZA(t):
    r'ACTUALIZA'
    return t


def t_SETEA(t):
    r'SETEA'
    return t


def t_BORRA_DE_LA(t):
    r'BORRA\s+DE\s+LA'
    return t


def t_MEZCLANDO(t):
    r'MEZCLANDO'
    return t


def t_EN(t):
    r'EN'
    t.type = 'EN'
    return t


def t_AGRUPANDO_POR(t):
    r'AGRUPANDO\s+POR'
    return t


def t_WHERE_DEL_GROUP_BY(t):
    r'WHERE\s+DEL\s+GROUP\s+BY'
    return t


def t_CAMBIA_LA_TABLA(t):
    r'CAMBIA\s+LA\s+TABLA'
    return t


def t_AGREGA_LA_COLUMNA(t):
    r'AGREGA\s+LA\s+COLUMNA'
    return t


def t_ELIMINA_LA_COLUMNA(t):
    r'ELIMINA\s+LA\s+COLUMNA'
    return t


def t_ENTRE(t):
    r'ENTRE'
    return t


def t_Y(t):
    r'Y'
    return t


def t_NO_NULO(t):
    r'NO\s+NULO'
    return t


def t_CONTANDO(t):
    r'CONTANDO'
    return t


def t_TODO(t):
    r'TODO'
    return t

# Identificadores y literales


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_STRING(t):
    r'\'([^\\\n]|(\\.))*?\''
    t.value = t.value[1:-1]  # Remover las comillas
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Manejo de nuevas líneas


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores


def t_error(t):
    raise SyntaxError(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()
