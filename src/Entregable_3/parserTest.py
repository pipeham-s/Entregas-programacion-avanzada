# test_is_usql.py
import unittest
from lexer import lexer
from parser import is_usql, parser  # Asegúrate de importar la función is_usql


def is_usql_test(query):
    lexer.input(query)
    tokens_list = list(lexer)
    return is_usql(tokens_list)

# Clase de pruebas unitarias usando unittest


class TestParser(unittest.TestCase):

    def test_is_usql_usql_query(self):
        query = "TRAEME LOS DISTINTOS nombre DE_LA_TABLA clientes DONDE ciudad = 'Madrid';"
        result = is_usql_test(query)
        self.assertTrue(result)

    def test_is_usql_sql_query(self):
        query = "SELECT * FROM customers WHERE city = 'Madrid';"
        result = is_usql_test(query)
        self.assertFalse(result)

    # Función para probar una consulta específica
    def run_query_test(self, query, expected_output):
        lexer.input(query)
        result = parser.parse(query)
        self.assertEqual(result, expected_output)

    # Prueba para cada consulta USQL
    def test_select_query(self):
        query = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        expected_output = "SELECT * FROM usuarios WHERE edad > 18;"
        self.run_query_test(query, expected_output)

    def test_distinct_query(self):
        query = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"
        expected_output = "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid';"
        self.run_query_test(query, expected_output)

    def test_insert_query(self):
        query = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        expected_output = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);"
        self.run_query_test(query, expected_output)

    def test_update_query(self):
        query = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        expected_output = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero';"
        self.run_query_test(query, expected_output)

    def test_join_query(self):
        query = "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';"
        expected_output = "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona';"
        self.run_query_test(query, expected_output)

    def test_group_by_query(self):
        query = "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;"
        expected_output = "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;"
        self.run_query_test(query, expected_output)

    def test_delete_query(self):
        query = "BORRA DE LA clientes DONDE edad ENTRE 18 Y 25;"
        expected_output = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25;"
        self.run_query_test(query, expected_output)

    def test_alter_add_column_query(self):
        query = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;"
        expected_output = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;"
        self.run_query_test(query, expected_output)

    def test_alter_drop_column_query(self):
        query = "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
        expected_output = "ALTER TABLE empleados DROP COLUMN direccion;"
        self.run_query_test(query, expected_output)


# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()