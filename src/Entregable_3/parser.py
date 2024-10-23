import ply.yacc as yacc
from lexer import lexer, tokens

# Función para determinar si la consulta es SQL o USQL


def is_usql(tokens_list):
    usql_keywords = {'TRAEME', 'METE_EN',
                     'ACTUALIZA', 'BORRA_DE_LA', 'CAMBIA_LA_TABLA'}
    return any(tok.type in usql_keywords for tok in tokens_list)

# Parser rules

# Funcion raiz


def p_statement(p):
    '''statement : usql_statement'''

    p[0] = p[1]

# USQL statement


def p_usql_statement(p):
    '''usql_statement : usql_select_statement
                      | usql_insert_statement
                      | usql_update_statement
                      | usql_delete_statement
                      | usql_alter_table_statement'''
    p[0] = p[1]

# SQL statement


# def p_sql_statement(p):
#     '''sql_statement : sql_select_statement
#                      | sql_insert_statement
#                      | sql_update_statement
#                      | sql_delete_statement
#                      | sql_alter_table_statement'''
#     p[0] = p[1]


# USQL select statement

def p_usql_select_statement(p):
    '''usql_select_statement : TRAEME select_elements DE_LA_TABLA table_reference optional_usql_join optional_usql_where optional_usql_group_by SEMICOLON'''
    p[0] = f"SELECT {p[2]} FROM {p[4]}{p[5]}{p[6]}{p[7]};"


# USQL insert statement

def p_insert_statement_usql(p):
    '''usql_insert_statement : METE_EN IDENTIFIER LPAREN column_list RPAREN LOS_VALORES LPAREN value_list RPAREN SEMICOLON'''
    table = p[2]  # Nombre de la tabla
    columns = p[4]  # Lista de columnas
    values = p[8]  # Lista de valores

    # Construcción de la consulta SQL
    p[0] = f"INSERT INTO {table} ({columns}) VALUES ({values});"

# USQL update statement


def p_update_statement_usql(p):
    '''usql_update_statement : ACTUALIZA IDENTIFIER SETEA set_list optional_usql_where SEMICOLON'''
    table = p[2]  # Nombre de la tabla
    set_clause = p[4]  # Lista de asignaciones (SET)
    where_clause = p[5]  # Condición WHERE opcional

    # Construcción de la consulta SQL
    p[0] = f"UPDATE {table} SET {set_clause}{where_clause};"


# USQL delete statement

def p_delete_statement_usql(p):
    '''usql_delete_statement : BORRA_DE_LA IDENTIFIER optional_usql_where SEMICOLON'''
    table = p[2]  # Nombre de la tabla
    where_clause = p[3]  # Condición WHERE opcional

    # Construcción de la consulta SQL
    p[0] = f"DELETE FROM {table}{where_clause};"


# USQL alter table statement

def p_alter_table_statement_usql(p):
    '''usql_alter_table_statement : CAMBIA_LA_TABLA IDENTIFIER alter_action_usql SEMICOLON'''
    table = p[2]  # Nombre de la tabla
    action = p[3]  # Acción de ALTER (ADD/DROP COLUMN)

    # Construcción de la consulta SQL
    p[0] = f"ALTER TABLE {table} {action};"


# alter action usql

def p_alter_action_usql(p):
    '''alter_action_usql : AGREGA_LA_COLUMNA IDENTIFIER data_type nullable
                         | ELIMINA_LA_COLUMNA IDENTIFIER'''
    if p[1] == 'AGREGA_LA_COLUMNA':
        nullable = f" {p[4]}" if p[4] else ''
        p[0] = f"ADD COLUMN {p[2]} {p[3]}{nullable}"
    else:
        p[0] = f"DROP COLUMN {p[2]}"

# data type


def p_data_type(p):
    '''data_type : IDENTIFIER LPAREN NUMBER RPAREN'''
    p[0] = f"{p[1]}({p[3]})"


# no nullable

def p_nullable(p):
    '''nullable : NO_NULO
                | empty'''
    p[0] = 'NOT NULL' if p[1] else ''

# Set de asignaciones (para UPDATE)


def p_set_list(p):
    '''set_list : assignment
                | set_list COMMA assignment'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"


# set de asignaciones (para UPDATE)

def p_assignment(p):
    '''assignment : IDENTIFIER EQUALS value'''
    p[0] = f"{p[1]} = {p[3]}"


# Elementos de SELECT usql


def p_select_elements(p):
    '''select_elements : TODO
                       | LOS_DISTINTOS select_list
                       | CONTANDO LPAREN TODO RPAREN
                       | select_list'''

    print(f"Contenido de p: {p[:]}")
    print(f"Token actual: {p[1]} (Tipo: {p.slice[1].type})")
    if p[1] == 'TODO':
        p[0] = '*'
    elif p.slice[1].type == 'LOS_DISTINTOS':
        p[0] = f"DISTINCT {p[2]}"
    elif p[1] == 'CONTANDO':
        p[0] = 'COUNT(*)'
    else:
        p[0] = p[1]

# Manejo de lista de selección


def p_select_list(p):
    '''select_list : IDENTIFIER
                   | select_list COMMA IDENTIFIER'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"


# Regla para table_reference
def p_table_reference(p):
    '''table_reference : IDENTIFIER'''
    p[0] = p[1]

# Cláusula opcional USQL JOIN (MEZCLANDO)


def p_optional_usql_join(p):
    '''optional_usql_join : MEZCLANDO table_reference EN condition
                          | empty'''
    if len(p) > 2:
        p[0] = f" JOIN {p[2]} ON {p[4]}"
    else:
        p[0] = ''

# Cláusula opcional WHERE (DONDE)


def p_optional_usql_where(p):
    '''optional_usql_where : DONDE condition
                           | empty'''
    if len(p) > 2:
        p[0] = f" WHERE {p[2]}"
    else:
        p[0] = ''

# Cláusula opcional GROUP BY (AGRUPANDO_POR)


def p_optional_usql_group_by(p):
    '''optional_usql_group_by : AGRUPANDO_POR group_list WHERE_DEL_GROUP_BY condition
                              | empty'''
    if len(p) > 2:
        p[0] = f" GROUP BY {p[2]} HAVING {p[4]}"
    else:
        p[0] = ''


# Lista de agrupación (para GROUP BY)


def p_group_list(p):
    '''group_list : IDENTIFIER
                  | group_list COMMA IDENTIFIER'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"

# Lista de columnas (para INSERT)


def p_column_list(p):
    '''column_list : IDENTIFIER
                   | column_list COMMA IDENTIFIER'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"

# Lista de valores (para INSERT)


def p_value_list(p):
    '''value_list : value
                  | value_list COMMA value'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"


# Valor (para INSERT)

def p_value(p):
    '''value : NUMBER
             | STRING'''
    if isinstance(p[1], int):
        p[0] = str(p[1])
    else:
        p[0] = f"'{p[1]}'"


# Condiciones (para WHERE y JOIN)


def p_condition(p):
    '''condition : expression comparator expression
                 | expression BETWEEN expression AND expression
                 | expression ENTRE expression Y expression
                 | expression'''
    if len(p) == 4:
        p[0] = f"{p[1]} {p[2]} {p[3]}"
    elif len(p) == 6 and p[2] in ('BETWEEN', 'ENTRE'):
        p[0] = f"{p[1]} BETWEEN {p[3]} AND {p[5]}"
    else:
        p[0] = p[1]


# Expresiones


def p_expression(p):
    '''expression : IDENTIFIER
                  | IDENTIFIER DOT IDENTIFIER
                  | NUMBER
                  | STRING'''
    if len(p) == 2:
        # Caso simple: IDENTIFIER, NUMBER, o STRING
        p[0] = p[1]
    elif len(p) == 4:
        # Caso: IDENTIFIER DOT IDENTIFIER (por ejemplo: pedidos.cliente_id)
        p[0] = f"{p[1]}.{p[3]}"

# Comparadores


def p_comparator(p):
    '''comparator : EQUALS
                  | GREATER_THAN
                  | LESS_THAN
                  | GE
                  | LE
                  | NE'''
    p[0] = p[1]

# Manejo de vacío


def p_empty(p):
    'empty :'
    p[0] = ''

# Manejo de errores de sintaxis


def p_error(p):
    raise SyntaxError(f"Error de sintaxis en la línea {p.lineno}")


# Crear el parser
parser = yacc.yacc()

# Crear el lexer


# Función para traducir la consulta
def translate_query(query):
    try:
        lexer.input(query)
        print(list(lexer))

        # Parsear la consulta
        result = parser.parse(query)
        return result
    except SyntaxError as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    queries = [
        "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;",
        "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';",
        "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';",
        "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);",
        "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;",

    ]

    ''',
        ,
        "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';",
        
        
        "BORRA_DE_LA clientes DONDE edad ENTRE 18 Y 25;",
        "CAMBIA_LA_TABLA empleados AGREGA_LA_COLUMNA direccion VARCHAR(255) NO_NULO;",
        "CAMBIA_LA_TABLA empleados ELIMINA_LA_COLUMNA direccion;" '''

    for query in queries:
        print(f"Probando la consulta: {query}")
        translated_query = translate_query(query)
        print(f"Resultado: {translated_query}\n")
