import sqlite3
from lexer import lexer  # Tu lexer de USQL
from parser import parser  # Tu parser de USQL a SQL

class USQLQueryBuilder:
    def __init__(self, db_path):
        self.db_path = db_path
        self.query = ""
        self.usql_query = ""
    
    def from_usql(self, usql_query):
        """Establece la consulta USQL inicial."""
        self.usql_query = usql_query
        self.query = self.translate_to_sql(usql_query)
        return self

    def translate_to_sql(self, usql_query):
        """Traduce la consulta de USQL a SQL utilizando el parser."""
        lexer.input(usql_query)
        try:
            sql_query = parser.parse(usql_query)
            return sql_query
        except SyntaxError as e:
            print(f"Error de traducción: {e}")
            return None

    def execute(self):
        """Ejecuta la consulta SQL traducida en la base de datos."""
        if not self.query:
            raise ValueError("No se ha configurado una consulta SQL válida.")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(self.query)
            if self.query.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
            else:
                conn.commit()
                result = cursor.rowcount
            print("Consulta ejecutada con éxito.")
            return result
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
    
    def to_sql(self):
        """Devuelve la consulta SQL traducida."""
        return self.query

# Ejemplo de uso:
if __name__ == "__main__":
    db_path = "mi_base_de_datos.db"  # Ruta de la base de datos SQLite
    builder = USQLQueryBuilder(db_path)

    # Consulta de ejemplo en USQL
    usql_query = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"

    # Crear la consulta con el builder, traducirla, y ejecutarla
    resultado = builder.from_usql(usql_query).execute()
    print("Resultado:", resultado)
