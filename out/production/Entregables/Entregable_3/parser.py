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
    '''statement : usql_statement
                 |  sql_statement'''

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


def p_sql_statement(p):
    '''sql_statement : sql_select_statement
                     | sql_insert_statement
                     | sql_update_statement
                     | sql_delete_statement
                     | sql_alter_table_statement'''
    p[0] = p[1]


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
    if p.slice[1].type == 'AGREGA_LA_COLUMNA':
        nullable = f" {p[4]}" if p[4] else ''
        p[0] = f"ADD COLUMN {p[2]} {p[3]}{nullable}"
    else:
        p[0] = f"DROP COLUMN {p[2]}"

# data type


def p_data_type(p):
    '''data_type : IDENTIFIER LPAREN NUMBER RPAREN
                 | VARCHAR LPAREN NUMBER RPAREN'''
    if p[1] == 'VARCHAR':
        p[0] = f"VARCHAR({p[3]})"
    p[0] = f"{p[1]}({p[3]})"


# no nullable

def p_nullable(p):
    '''nullable : NO_NULO
                | NOT_NULL
                | empty'''
    if p.slice[1].type == 'NO_NULO':
        p[0] = 'NOT NULL'
    elif p.slice[1].type == 'NOT_NULL':
        p[0] = 'NO NULO'
    else:
        p[0] = ''

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

    # print(f"Contenido de p: {p[:]}")
    # print(f"Token actual: {p[1]} (Tipo: {p.slice[1].type})")
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
                              | GROUP_BY group_list HAVING condition
                              | AGRUPANDO_POR group_list
                              | GROUP_BY group_list
                              | empty'''

    if len(p) == 3:
        # Si solo tiene `GROUP BY` o `AGRUPANDO POR` sin `HAVING`
        if p.slice[1].type == 'AGRUPANDO_POR':
            p[0] = f" GROUP BY {p[2]}"
        else:
            p[0] = f" AGRUPANDO POR {p[2]}"
    elif len(p) == 5:
        # Si tiene `GROUP BY ... HAVING` o `AGRUPANDO POR ... WHERE DEL GROUP BY`
        if p.slice[1].type == 'AGRUPANDO_POR':
            p[0] = f" GROUP BY {p[2]} HAVING {p[4]}"
        else:
            p[0] = f" AGRUPANDO POR {p[2]} WHERE DEL GROUP BY {p[4]}"
    else:
        # Caso de `empty`
        p[0] = ''


# Lista de agrupación (para GROUP BY)


def p_group_list(p):
    '''group_list : IDENTIFIER
                  | IDENTIFIER COMMA IDENTIFIER
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
        # Mantener las comillas simples correctamente sin duplicarlas
        p[0] = p[1]  # Elimina cualquier procesamiento adicional de comillas


# Condiciones (para WHERE y JOIN)


# Condiciones (para WHERE y JOIN)
def p_condition(p):
    '''condition : expression comparator expression
                 | expression BETWEEN expression AND expression
                 | expression ENTRE expression Y expression
                 | expression'''
    if len(p) == 4 and p[2] in ('=', '>', '<', '>=', '<=', '<>'):
        p[0] = f"{p[1]} {p[2]} {p[3]}"
    elif len(p) == 6:

        # Maneja ambas versiones para SQL y USQL
        if p[2] == 'BETWEEN':
            p[0] = f"{p[1]} ENTRE {p[3]} Y {p[5]}"
        else:
            p[0] = f"{p[1]} BETWEEN {p[3]} AND {p[5]}"

    else:
        p[0] = p[1]


# Expresiones


def p_expression(p):
    '''expression : IDENTIFIER
                  | STRING
                  | NUMBER
                  | COUNT LPAREN ASTERISK RPAREN
                  | IDENTIFIER DOT IDENTIFIER'''
    if len(p) == 2:
        p[0] = str(p[1])
    elif len(p) == 5 and p[1] == 'COUNT':
        p[0] = 'COUNT(*)'
    elif len(p) == 4:
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


# AHORA EL MANEJO PARA TRADUCIR DE SQL A USQL

# SQL SELECT a USQL TRAEME
def p_sql_select_statement(p):
    '''sql_select_statement : SELECT select_elements_sql FROM table_reference optional_sql_join optional_sql_where optional_usql_group_by SEMICOLON'''
    # Traducción de SQL a USQL
    p[0] = f"TRAEME {p[2]} DE LA TABLA {p[4]}{p[5]}{p[6]}{p[7]};"

# SQL INSERT a USQL METE_EN


def p_sql_insert_statement(p):
    '''sql_insert_statement : INSERT_INTO IDENTIFIER LPAREN column_list RPAREN VALUES LPAREN value_list RPAREN SEMICOLON'''
    # Traducción de SQL a USQL
    p[0] = f"METE EN {p[2]} ({p[4]}) LOS VALORES ({p[8]});"

# SQL UPDATE a USQL ACTUALIZA


def p_sql_update_statement(p):
    '''sql_update_statement : UPDATE IDENTIFIER SET set_list optional_sql_where SEMICOLON'''
    # Traducción de SQL a USQL
    p[0] = f"ACTUALIZA {p[2]} SETEA {p[4]}{p[5]};"

# SQL DELETE a USQL BORRA_DE_LA


def p_sql_delete_statement(p):
    '''sql_delete_statement : DELETE_FROM IDENTIFIER optional_sql_where SEMICOLON'''
    # Traducción de SQL a USQL
    p[0] = f"BORRA DE LA {p[2]}{p[3]};"

# SQL ALTER TABLE a USQL CAMBIA_LA_TABLA


def p_sql_alter_table_statement(p):
    '''sql_alter_table_statement : ALTER_TABLE IDENTIFIER alter_action_sql SEMICOLON'''
    # Traducción de SQL a USQL
    p[0] = f"CAMBIA LA TABLA {p[2]} {p[3]};"

# Acción de alteración de columna en SQL a USQL


def p_alter_action_sql(p):
    '''alter_action_sql : ADD_COLUMN IDENTIFIER data_type nullable
                        | DROP_COLUMN IDENTIFIER'''
    if p.slice[1].type == 'ADD_COLUMN':
        nullable = f" {p[4]}" if p[4] else ''
        p[0] = f"AGREGA LA COLUMNA {p[2]} {p[3]}{nullable}"
    else:
        p[0] = f"ELIMINA LA COLUMNA {p[2]}"

# Elementos de SELECT SQL (similar a USQL)


def p_select_elements_sql(p):
    '''select_elements_sql : ASTERISK
                       | DISTINCT select_list
                       | COUNT LPAREN ASTERISK RPAREN
                       | select_list'''
    if p[1] == '*':
        p[0] = "TODO"
    elif p[1] == 'DISTINCT':
        p[0] = f"LOS DISTINTOS {p[2]}"
    elif p[1] == 'COUNT':
        p[0] = "CONTANDO(TODO)"
    else:
        p[0] = p[1]

# Reglas opcionales para SQL JOIN


def p_optional_sql_join(p):
    '''optional_sql_join : JOIN IDENTIFIER ON condition
                         | empty'''
    if len(p) > 2:
        p[0] = f" MEZCLANDO {p[2]} EN {p[4]}"
    else:
        p[0] = ''

# Reglas opcionales para SQL WHERE


def p_optional_sql_where(p):
    '''optional_sql_where : WHERE condition
                          | empty'''
    if len(p) > 2:
        p[0] = f" DONDE {p[2]}"
    else:
        p[0] = ''

# Reglas opcionales para SQL GROUP BY


# def p_optional_sql_group_by(p):
#     '''optional_sql_group_by : GROUP_BY group_list HAVING condition
#                              | empty'''
#     if len(p) > 2:
#         p[0] = f" AGRUPANDO POR {p[2]} WHERE DEL GROUP BY {p[4]}"
#     else:
#         p[0] = ''


# Crear el parser
parser = yacc.yacc()


# Crear el lexer


# Función para traducir la consulta
def translate_query(query):
    try:
        lexer.input(query)
        # print(list(lexer))

        # Parsear la consulta
        result = parser.parse(query)
        return result
    except SyntaxError as e:
        print(f"Error: {e}")
        return None


# if __name__ == '__main__':
    # queries = [
    #     "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;",
    #     "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';",
    #     "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';",
    #     "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);",
    #     "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;",
    #     "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';",
    #     "BORRA DE LA clientes DONDE edad ENTRE 18 Y 25;",
    #     "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;",
    #     "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
    # ]
    # sql_queries = [
    #     "SELECT * FROM usuarios WHERE edad > 18;",
    #     "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid';",
    #     "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona';",
    #     "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);",
    #     "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;",
    #     "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero';",
    #     "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25;",
    #     "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;",
    #     "ALTER TABLE empleados DROP COLUMN direccion;"
    # ]

    # for query in queries:
    #     print(f"Probando la consulta: {query}")
    #     translated_query = translate_query(query)
    #     print(f"Resultado: {translated_query}\n")

    # for query in sql_queries:
    #     print(f"Probando la consulta: {query}")
    #     translated_query = translate_query(query)
    #     print(f"Resultado: {translated_query}\n")
