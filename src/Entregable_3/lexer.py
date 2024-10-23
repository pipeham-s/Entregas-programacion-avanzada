import ply.lex as lex

# Diccionario de palabras clave y su mapeo entre SQL y USQL
usql_to_sql_keywords = {
    'TRAEME': 'SELECT',
    'TODO': '*',
    'DE_LA_TABLA': 'FROM',
    'DONDE': 'WHERE',
    'AGRUPANDO_POR': 'GROUP BY',
    'MEZCLANDO': 'JOIN',
    'EN': 'ON',
    'LOS_DISTINTOS': 'DISTINCT',
    'CONTANDO': 'COUNT',
    'METE_EN': 'INSERT INTO',
    'LOS_VALORES': 'VALUES',
    'ACTUALIZA': 'UPDATE',
    'SETEA': 'SET',
    'BORRA_DE_LA': 'DELETE FROM',
    'ORDENA_POR': 'ORDER BY',
    'COMO_MUCHO': 'LIMIT',
    'WHERE_DEL_GROUP_BY': 'HAVING',
    'EXISTE': 'EXISTS',
    'EN_ESTO': 'IN',
    'ENTRE': 'BETWEEN',
    'PARECIDO_A': 'LIKE',
    'ES_NULO': 'IS NULL',
    'CAMBIA_LA_TABLA': 'ALTER TABLE',
    'AGREGA_LA_COLUMNA': 'ADD COLUMN',
    'ELIMINA_LA_COLUMNA': 'DROP COLUMN',
    'CREA_LA_TABLA': 'CREATE TABLE',
    'TIRA_LA_TABLA': 'DROP TABLE',
    'POR_DEFECTO': 'DEFAULT',
    'UNICO': 'UNIQUE',
    'CLAVE_PRIMA': 'PRIMARY KEY',
    'CLAVE_REFERENTE': 'FOREIGN KEY',
    'NO_NULO': 'NOT NULL',
    'TRANSFORMA_A': 'CAST',
}

sql_to_usql_keywords = {v: k for k, v in usql_to_sql_keywords.items()}

# Lista de tokens
tokens = [
    'IDENTIFIER',
    'STRING',
    'NUMBER',
    'COMMA',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'EQ',
    'GT',
    'LT',
    'GE',
    'LE',
    'NE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'AND',
    'OR',
    'NOT',
    'DOT',
    'ASTERISK',
] + list(usql_to_sql_keywords.keys())

# Expresiones regulares para tokens simples
t_COMMA = r','
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQ = r'='
t_GT = r'>'
t_LT = r'<'
t_GE = r'>='
t_LE = r'<='
t_NE = r'<>|!='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_DOT = r'\.'
t_ASTERISK = r'\*'

# Ignoramos espacios y tabs
t_ignore = ' \t'

# Palabras reservadas (tanto USQL como SQL)
reserved = set(usql_to_sql_keywords.keys()) | set(
    usql_to_sql_keywords.values())


def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    upper_value = t.value.upper()
    if upper_value in reserved:
        t.type = upper_value  # Es una palabra clave
    else:
        t.type = 'IDENTIFIER'
    t.value = t.value
    return t


def t_STRING(t):
    r'\'[^\']*\'|"[^"]*"'
    t.value = t.value.strip('\'"')
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_AND(t):
    r'AND|Y'
    t.type = 'AND'
    return t


def t_OR(t):
    r'OR|O'
    t.type = 'OR'
    return t


def t_NOT(t):
    r'NOT|NO'
    t.type = 'NOT'
    return t


def t_error(t):
    raise SyntaxError(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()
