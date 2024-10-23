import ply.yacc as yacc
from usql_lexer import tokens, usql_to_sql_keywords, sql_to_usql_keywords, lexer

# Definimos la gramática


def p_statement(p):
    '''statement : statement_usql
                 | statement_sql'''
    p[0] = p[1]


def p_statement_usql(p):
    '''statement_usql : usql_query'''
    p[0] = translate_usql_to_sql(p[1])


def p_statement_sql(p):
    '''statement_sql : sql_query'''
    p[0] = translate_sql_to_usql(p[1])


def p_usql_query(p):
    '''usql_query : usql_select_statement
                  | usql_insert_statement
                  | usql_update_statement
                  | usql_delete_statement
                  | usql_alter_statement
                  | usql_create_statement
                  | usql_drop_statement'''
    p[0] = p[1]


def p_sql_query(p):
    '''sql_query : sql_select_statement
                 | sql_insert_statement
                 | sql_update_statement
                 | sql_delete_statement
                 | sql_alter_statement
                 | sql_create_statement
                 | sql_drop_statement'''
    p[0] = p[1]

# Aquí agregaríamos las reglas para cada tipo de sentencia en USQL y SQL
# Por simplicidad, mostraré solo el select_statement


def p_usql_select_statement(p):
    '''usql_select_statement : TRAEME usql_select_elements DE_LA_TABLA table_references usql_optional_where usql_optional_group_by usql_optional_having usql_optional_order_by SEMICOLON'''
    p[0] = {
        'type': 'SELECT',
        'elements': p[2],
        'from': p[4],
        'where': p[5],
        'group_by': p[6],
        'having': p[7],
        'order_by': p[8]
    }


def p_sql_select_statement(p):
    '''sql_select_statement : SELECT sql_select_elements FROM table_references sql_optional_where sql_optional_group_by sql_optional_having sql_optional_order_by SEMICOLON'''
    p[0] = {
        'type': 'SELECT',
        'elements': p[2],
        'from': p[4],
        'where': p[5],
        'group_by': p[6],
        'having': p[7],
        'order_by': p[8]
    }


def p_usql_select_elements(p):
    '''usql_select_elements : TODO
                            | LOS_DISTINTOS select_list
                            | select_list'''
    if p[1] == 'TODO':
        p[0] = '*'
    elif p[1] == 'LOS_DISTINTOS':
        p[0] = 'DISTINCT ' + p[2]
    else:
        p[0] = p[1]


def p_sql_select_elements(p):
    '''sql_select_elements : ASTERISK
                           | DISTINCT select_list
                           | select_list'''
    if p[1] == '*':
        p[0] = '*'
    elif p[1] == 'DISTINCT':
        p[0] = 'DISTINCT ' + p[2]
    else:
        p[0] = p[1]


def p_select_list(p):
    '''select_list : select_item
                   | select_item COMMA select_list'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ', ' + p[3]


def p_select_item(p):
    '''select_item : IDENTIFIER'''
    p[0] = p[1]


def p_table_references(p):
    '''table_references : IDENTIFIER
                        | IDENTIFIER MEZCLANDO IDENTIFIER EN condition
                        | IDENTIFIER JOIN IDENTIFIER ON condition'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        join_type = 'JOIN' if p[2] in ('MEZCLANDO', 'JOIN') else p[2]
        on_keyword = 'ON' if p[4] in ('EN', 'ON') else p[4]
        p[0] = f"{p[1]} {join_type} {p[3]} {on_keyword} {p[5]}"


def p_usql_optional_where(p):
    '''usql_optional_where : DONDE condition
                           | empty'''
    p[0] = f"WHERE {p[2]}" if len(p) > 2 else ''


def p_sql_optional_where(p):
    '''sql_optional_where : WHERE condition
                          | empty'''
    p[0] = f"WHERE {p[2]}" if len(p) > 2 else ''


def p_usql_optional_group_by(p):
    '''usql_optional_group_by : AGRUPANDO_POR group_list
                              | empty'''
    p[0] = f"GROUP BY {p[2]}" if len(p) > 2 else ''


def p_sql_optional_group_by(p):
    '''sql_optional_group_by : GROUP BY group_list
                             | empty'''
    if len(p) > 2:
        p[0] = 'GROUP BY ' + p[3]
    else:
        p[0] = ''


def p_group_list(p):
    '''group_list : IDENTIFIER
                  | IDENTIFIER COMMA group_list'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ', ' + p[3]


def p_usql_optional_having(p):
    '''usql_optional_having : WHERE_DEL_GROUP_BY condition
                            | empty'''
    p[0] = f"HAVING {p[2]}" if len(p) > 2 else ''


def p_sql_optional_having(p):
    '''sql_optional_having : HAVING condition
                           | empty'''
    p[0] = f"HAVING {p[2]}" if len(p) > 2 else ''


def p_usql_optional_order_by(p):
    '''usql_optional_order_by : ORDENA_POR order_list
                              | empty'''
    p[0] = f"ORDER BY {p[2]}" if len(p) > 2 else ''


def p_sql_optional_order_by(p):
    '''sql_optional_order_by : ORDER BY order_list
                             | empty'''
    if len(p) > 2:
        p[0] = 'ORDER BY ' + p[3]
    else:
        p[0] = ''


def p_order_list(p):
    '''order_list : IDENTIFIER
                  | IDENTIFIER COMMA order_list'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + ', ' + p[3]


def p_condition(p):
    '''condition : expression comparator expression
                 | expression BETWEEN expression AND expression
                 | expression ENTRE expression Y expression
                 | LPAREN condition RPAREN
                 | condition AND condition
                 | condition OR condition
                 | NOT condition'''
    if len(p) == 4 and p[2] in ('=', '>', '<', '>=', '<=', '<>', '!='):
        p[0] = f"{p[1]} {p[2]} {p[3]}"
    elif p[2] in ('BETWEEN', 'ENTRE'):
        and_keyword = 'AND' if p[4] in ('AND', 'Y') else p[4]
        p[0] = f"{p[1]} BETWEEN {p[3]} {and_keyword} {p[5]}"
    elif p[1] == '(':
        p[0] = f"({p[2]})"
    elif p[2] in ('AND', 'OR'):
        p[0] = f"{p[1]} {p[2]} {p[3]}"
    elif p[1] == 'NOT':
        p[0] = f"NOT {p[2]}"


def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | STRING'''
    p[0] = str(p[1])


def p_comparator(p):
    '''comparator : EQ
                  | GT
                  | LT
                  | GE
                  | LE
                  | NE'''
    p[0] = p[1]


def p_empty(p):
    'empty :'
    p[0] = ''


def p_error(p):
    if p:
        raise SyntaxError(f"Error de sintaxis en '{
                          p.value}' en la línea {p.lineno}")
    else:
        raise SyntaxError("Error de sintaxis al final de la entrada")


parser = yacc.yacc()

# Funciones de traducción


def translate_usql_to_sql(parsed_query):
    # Convertimos el árbol de sintaxis abstracta a una cadena SQL
    if parsed_query['type'] == 'SELECT':
        elements = parsed_query['elements']
        from_clause = parsed_query['from']
        where_clause = parsed_query['where']
        group_by_clause = parsed_query['group_by']
        having_clause = parsed_query['having']
        order_by_clause = parsed_query['order_by']
        sql_query = f"SELECT {elements} FROM {from_clause} {where_clause} {
            group_by_clause} {having_clause} {order_by_clause};"
        return sql_query.strip()
    # Implementar otros tipos de sentencias
    return ''


def translate_sql_to_usql(parsed_query):
    # Convertimos el árbol de sintaxis abstracta a una cadena USQL
    if parsed_query['type'] == 'SELECT':
        elements = parsed_query['elements']
        from_clause = parsed_query['from']
        where_clause = parsed_query['where']
        group_by_clause = parsed_query['group_by']
        having_clause = parsed_query['having']
        order_by_clause = parsed_query['order_by']
        elements_usql = elements.replace(
            'DISTINCT', 'LOS_DISTINTOS') if 'DISTINCT' in elements else elements
        usql_query = f"TRAEME {elements_usql} DE_LA_TABLA {from_clause} {
            where_clause} {group_by_clause} {having_clause} {order_by_clause};"
        return usql_query.strip()
    # Implementar otros tipos de sentencias
    return ''
