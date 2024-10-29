import sqlite3
from parser import translate_query, is_usql
from lexer import lexer
import re


def clean_query(query):
    """Limpia y formatea la consulta de entrada."""
    # Reemplaza múltiples espacios por uno solo
    query = re.sub(r'\s+', ' ', query)
    # Remueve espacios innecesarios alrededor de caracteres especiales
    query = query.strip()
    return query


class FluentQueryAPI:
    def __init__(self, db_path):
        self.db_path = db_path

    def execute_query(self, query):
        query = clean_query(query)  # Asegura un formato uniforme del query
        lexer.input(query)
        tokens_list = list(lexer)

        is_usql_query = is_usql(tokens_list)
        print("\n" + "="*50)
        print(f"Probando traducir la consulta:\n{query}")

        if is_usql_query:
            print("Lenguaje USQL detectado, traduciendo a SQL...")
            translated_query = translate_query(query)
            if translated_query:
                print(f"Traducción a SQL:\n{translated_query}")
                print("Ejecutando sentencia traducida en SQL...")
                self._execute(translated_query)
            else:
                print(
                    "Error en la traducción de USQL a SQL. No se ejecutará la consulta.")
        else:
            print("Lenguaje SQL detectado, traduciendo a USQL...")
            translated_query = translate_query(query)
            if translated_query:
                print(f"Traducción a USQL (no ejecutada):\n{translated_query}")
            print("Ejecutando sentencia original en SQL...")
            self._execute(query)
        print("="*50 + "\n")

    def _execute(self, sql_query):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(sql_query)
                results = cursor.fetchall()
                for row in results:
                    print(row)
                conn.commit()
        except sqlite3.Error as e:
            print("Error ejecutando la consulta en SQL:", e)


# Inicializar la base de datos y la API
db_path = "mi_base_de_datos.db"
api = FluentQueryAPI(db_path)

api.execute_query("TRAEME TODO DE LA TABLA usuarios;")

# Loop para recibir consultas desde la consola
while True:
    query = input("Ingrese una consulta (o 'salir' para terminar): ").strip()
    print(f"Consulta ingresada: '{query}'")
    if query.strip().lower() == 'salir':
        print("Saliendo del programa.")
        break
    api.execute_query(query)
