import ply.yacc as yacc
import ply.lex as lex

# Definir los tokens para SQL y USQL
tokens = [
    'SELECT', 'TRAEME', 'FROM', 'DE_LA_TABLA', 'WHERE', 'DONDE',
    'INSERT_INTO', 'METE_EN', 'VALUES', 'LOS_VALORES', 'UPDATE',
    'ACTUALIZA', 'SET', 'SETEA', 'DELETE_FROM', 'BORRA_DE_LA',
    'ORDER_BY', 'ORDENA_POR', 'GROUP_BY', 'AGRUPANDO_POR', 'JOIN',
    'MEZCLANDO', 'ON', 'EN', 'DISTINCT', 'LOS_DISTINTOS', 'COUNT',
    'CONTANDO', 'LIMIT', 'COMO_MUCHO', 'HAVING', 'WHERE_DEL_GROUP_BY',
    'EXISTS', 'IN_ESTO', 'BETWEEN', 'ENTRE', 'LIKE', 'PARECIDO_A',
    'IS_NULL', 'ES_NULO', 'ALTER_TABLE', 'CAMBIA_LA_TABLA',
    'ADD_COLUMN', 'AGREGA_LA_COLUMNA', 'DROP_COLUMN', 'ELIMINA_LA_COLUMNA',
    'CREATE_TABLE', 'CREA_LA_TABLA', 'DROP_TABLE', 'TIRA_LA_TABLA',
    'DEFAULT', 'POR_DEFECTO', 'UNIQUE', 'UNICO', 'PRIMARY_KEY', 'CLAVE_PRIMA',
    'FOREIGN_KEY', 'CLAVE_REFERENTE', 'NOT_NULL', 'NO_NULO', 'CAST', 'TRANSFORMA_A',
    'TODO',  '*',
    'NUMBER', 'IDENTIFIER', 'STRING', 'EQUALS', 'GREATER_THAN', 'LESS_THAN',
    'VARCHAR', 'INT', 'FLOAT', 'DATE', 'BOOLEAN', 'TEXT', 'NUMBER'
]

# Reglas léxicas para identificar los tokens
t_SELECT = r'SELECT'
t_TRAEME = r'TRAEME'
t_FROM = r'FROM'
t_DE_LA_TABLA = r'DE LA TABLA'
t_WHERE = r'WHERE'
t_DONDE = r'DONDE'
t_INSERT_INTO = r'INSERT INTO'
t_METE_EN = r'METE EN'
t_VALUES = r'VALUES'
t_LOS_VALORES = r'LOS VALORES'
t_UPDATE = r'UPDATE'
t_ACTUALIZA = r'ACTUALIZA'
t_SET = r'SET'
t_SETEA = r'SETEA'
t_DELETE_FROM = r'DELETE FROM'
t_BORRA_DE_LA = r'BORRA DE LA'
t_ORDER_BY = r'ORDER BY'
t_ORDENA_POR = r'ORDENA POR'
t_GROUP_BY = r'GROUP BY'
t_AGRUPANDO_POR = r'AGRUPANDO POR'
t_JOIN = r'JOIN'
t_MEZCLANDO = r'MEZCLANDO'
t_ON = r'ON'
t_EN = r'EN'
t_DISTINCT = r'DISTINCT'
t_LOS_DISTINTOS = r'LOS DISTINTOS'
t_COUNT = r'COUNT'
t_CONTANDO = r'CONTANDO'
t_LIMIT = r'LIMIT'
t_COMO_MUCHO = r'COMO MUCHO'
t_TODO = r'\*'

t_EQUALS = r'='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'

t_NUMBER = r'\d+'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_STRING = r"'([^\\']|\\.)*'"  # Cadena de texto con comillas simples

t_VARCHAR = r'VARCHAR'
t_INT = r'INT'
t_FLOAT = r'FLOAT'
t_DATE = r'DATE'
t_BOOLEAN = r'BOOLEAN'
t_TEXT = r'TEXT'
t_NO_NULO = r'NO NULO'
t_UNIQUE = r'UNIQUE'
t_PRIMARY_KEY = r'PRIMARY KEY'
t_FOREIGN_KEY = r'FOREIGN KEY'
t_DEFAULT = r'DEFAULT'
t_CHECK = r'CHECK'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de saltos de línea


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Manejo de errores léxicos


def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)


# Construir el lexer
lexer = lex.lex()


# Definir las reglas gramaticales para el parser

def p_statement_select(t):
    '''statement : SELECT columns FROM table WHERE condition
                 | TRAEME columns DE_LA_TABLA table DONDE condition'''
    if t[1] == 'SELECT':
        if t[2] == '*':
            t[0] = f'TRAEME TODO DE LA TABLA {t[4]} DONDE {t[6]}'
        else:
            t[0] = f'TRAEME {t[2]} DE LA TABLA {t[4]} DONDE {t[6]}'
    else:
        if t[2] == 'TODO':
            t[0] = f'SELECT * FROM {t[4]} WHERE {t[6]}'
        else:
            t[0] = f'SELECT {t[2]} FROM {t[4]} WHERE {t[6]}'


def p_statement_distinct(t):
    '''statement : SELECT DISTINCT columns FROM table WHERE condition
                 | TRAEME LOS_DISTINTOS columns DE_LA_TABLA table DONDE condition'''
    if t[1] == 'SELECT':
        t[0] = f'TRAEME LOS DISTINTOS {t[3]} DE LA TABLA {t[5]} DONDE {t[7]}'
    else:
        t[0] = f'SELECT DISTINCT {t[3]} FROM {t[5]} WHERE {t[7]}'


def p_statement_insert(t):
    '''statement : INSERT_INTO table LPAREN column_list RPAREN VALUES LPAREN value_list RPAREN
                 | METE_EN table LPAREN column_list RPAREN LOS_VALORES LPAREN value_list RPAREN'''
    if t[1] == 'INSERT INTO':
        t[0] = f"METE EN {t[2]} ({t[4]}) LOS VALORES ({t[8]})"
    else:
        t[0] = f"INSERT INTO {t[2]} ({t[4]}) VALUES ({t[8]})"


def p_statement_update(t):
    '''statement : UPDATE table SET assignments WHERE condition
                 | ACTUALIZA table SETEA assignments DONDE condition'''
    if t[1] == 'UPDATE':
        t[0] = f"ACTUALIZA {t[2]} SETEA {t[4]} DONDE {t[6]}"
    else:
        t[0] = f"UPDATE {t[2]} SET {t[4]} WHERE {t[6]}"


def p_statement_delete(t):
    '''statement : DELETE_FROM table WHERE condition
                 | BORRA_DE_LA table DONDE condition'''
    if t[1] == 'DELETE FROM':
        t[0] = f"BORRA DE LA {t[2]} DONDE {t[4]}"
    else:
        t[0] = f"DELETE FROM {t[2]} WHERE {t[4]}"


def p_statement_join(t):
    '''statement : SELECT columns FROM table JOIN table ON condition WHERE condition
                 | TRAEME columns DE_LA_TABLA table MEZCLANDO table EN condition DONDE condition'''
    if t[1] == 'SELECT':
        t[0] = f"TRAEME {t[2]} DE LA TABLA {
            t[4]} MEZCLANDO {t[6]} EN {t[8]} DONDE {t[10]}"
    else:
        t[0] = f"SELECT {t[2]} FROM {t[4]} JOIN {t[6]} ON {t[8]} WHERE {t[10]}"


def p_statement_group_by(t):
    '''statement : SELECT COUNT LPAREN TODO RPAREN FROM table GROUP_BY column HAVING condition
                 | TRAEME CONTANDO LPAREN TODO RPAREN DE_LA_TABLA table AGRUPANDO_POR column WHERE_DEL_GROUP_BY condition'''
    if t[1] == 'SELECT':
        t[0] = f"TRAEME CONTANDO(TODO) DE LA TABLA {t[6]} AGRUPANDO POR {
            t[8]} WHERE DEL GROUP BY {t[10]}"
    else:
        t[0] = f"SELECT COUNT(*) FROM {t[6]} GROUP BY {t[8]} HAVING {t[10]}"


def p_statement_alter_table(t):
    '''statement : ALTER_TABLE table ADD_COLUMN IDENTIFIER data_type constraints
                 | CAMBIA_LA_TABLA table AGREGA_LA_COLUMNA IDENTIFIER data_type constraints
                 | ALTER_TABLE table DROP_COLUMN IDENTIFIER
                 | CAMBIA_LA_TABLA table ELIMINA_LA_COLUMNA IDENTIFIER'''
    if t[1] == 'ALTER TABLE':
        if t[3] == 'ADD COLUMN':
            t[0] = f"ALTER TABLE {t[2]} ADD COLUMN {t[4]} {t[5]} {t[6]}"
        else:
            t[0] = f"ALTER TABLE {t[2]} DROP COLUMN {t[4]}"
    else:
        if t[3] == 'AGREGA LA COLUMNA':
            t[0] = f"CAMBIA LA TABLA {
                t[2]} AGREGA LA COLUMNA {t[4]} {t[5]} {t[6]}"
        else:
            t[0] = f"CAMBIA LA TABLA {t[2]} ELIMINA LA COLUMNA {t[4]}"


# Reglas para columnas, tablas, condiciones, valores
def p_columns(t):
    '''columns : TODO
               | IDENTIFIER'''
    t[0] = t[1]


def p_table(t):
    '''table : IDENTIFIER'''
    t[0] = t[1]


def p_condition(t):
    '''condition : IDENTIFIER EQUALS value
                 | IDENTIFIER GREATER_THAN value
                 | IDENTIFIER LESS_THAN value
                 | IDENTIFIER LIKE value'''
    t[0] = f"{t[1]} {t[2]} {t[3]}"


def p_value(t):
    '''value : NUMBER
             | IDENTIFIER
             | STRING'''
    t[0] = t[1]


def p_column_list(t):
    '''column_list : IDENTIFIER
                   | IDENTIFIER COMMA column_list'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = f"{t[1]}, {t[3]}"


def p_value_list(t):
    '''value_list : value
                  | value COMMA value_list'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = f"{t[1]}, {t[3]}"


def p_assignments(t):
    '''assignments : IDENTIFIER EQUALS value
                   | IDENTIFIER EQUALS value COMMA assignments'''
    if len(t) == 4:
        t[0] = f"{t[1]} = {t[3]}"
    else:
        t[0] = f"{t[1]} = {t[3]}, {t[5]}"


def p_constraints(t):
    '''constraints : NOT_NULL
                   | UNIQUE
                   | PRIMARY_KEY
                   | FOREIGN_KEY LPAREN IDENTIFIER RPAREN
                   | DEFAULT value
                   | CHECK LPAREN condition RPAREN
                   | constraints constraints'''
    if len(t) == 2:
        t[0] = t[1]
    elif t[1] == 'FOREIGN KEY':
        t[0] = f"FOREIGN KEY({t[3]})"
    elif t[1] == 'CHECK':
        t[0] = f"CHECK({t[3]})"
    elif t[1] == 'DEFAULT':
        t[0] = f"DEFAULT {t[2]}"
    else:
        t[0] = f"{t[1]} {t[2]}"


def p_data_type(t):
    '''data_type : VARCHAR LPAREN NUMBER RPAREN
                 | INT
                 | FLOAT
                 | DATE
                 | BOOLEAN
                 | TEXT
                 | data_type constraints'''
    if len(t) == 2:
        t[0] = t[1]
    elif t[2] == '(':
        t[0] = f"{t[1]}({t[3]})"
    elif len(t) == 3:
        t[0] = f"{t[1]} {t[2]}"


# Manejo de errores sintácticos
def p_error(t):
    print(f"Error sintáctico en '{t.value}'")


# Construcción del parser
parser = yacc.yacc()


# Función para traducir consultas
def translate(query):
    return parser.parse(query)
