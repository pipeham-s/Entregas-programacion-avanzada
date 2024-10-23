# Diccionario de mapeo SQL -> USQL
sql_to_usql = {
    "SELECT": "TRAEME",
    "*": "TODO",
    "FROM": "DE LA TABLA",
    "WHERE": "DONDE",
    "GROUP BY": "AGRUPANDO POR",
    "JOIN": "MEZCLANDO",
    "ON": "EN",
    "DISTINCT": "LOS DISTINTOS",
    "COUNT": "CONTANDO",
    "INSERT INTO": "METE EN",
    "VALUES": "LOS VALORES",
    "UPDATE": "ACTUALIZA",
    "SET": "SETEA",
    "DELETE FROM": "BORRA DE LA",
    "ORDER BY": "ORDENA POR",
    "LIMIT": "COMO MUCHO",
    "HAVING": "WHERE DEL GROUP BY",
    "EXISTS": "EXISTE",
    "IN": "EN ESTO:",
    "BETWEEN": "ENTRE",
    "LIKE": "PARECIDO A",
    "IS NULL": "ES NULO",
    "ALTER TABLE": "CAMBIA LA TABLA",
    "ADD COLUMN": "AGREGA LA COLUMNA",
    "DROP COLUMN": "ELIMINA LA COLUMNA",
    "CREATE TABLE": "CREA LA TABLA",
    "DROP TABLE": "TIRA LA TABLA",
    "DEFAULT": "POR DEFECTO",
    "UNIQUE": "UNICO",
    "PRIMARY KEY": "CLAVE PRIMA",
    "FOREIGN KEY": "CLAVE REFERENTE",
    "NOT NULL": "NO NULO",
    "CAST": "TRANSFORMA A"
}

# Función para transformar SQL a USQL


def sql_to_usql_transformer(query: str) -> str:
    # Separamos las palabras para no tener problemas con tokens como "*" o palabras separadas
    for sql_word, usql_word in sql_to_usql.items():
        query = query.replace(sql_word, usql_word)
    return query


# Invertimos el diccionario para hacer la traducción inversa (USQL -> SQL)
usql_to_sql = {v: k for k, v in sql_to_usql.items()}

# Función para transformar USQL a SQL


def usql_to_sql_transformer(query: str) -> str:
    # Separamos las palabras para evitar problemas con tokens complejos
    for usql_word, sql_word in usql_to_sql.items():
        query = query.replace(usql_word, sql_word)
    return query


# Ejemplo de uso
sql_query = "SELECT * FROM table WHERE column = 'value'"
usql_query = sql_to_usql_transformer(sql_query)
print(usql_query)
