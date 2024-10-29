# test_is_usql.py
import unittest
from lexer import lexer
# Asegúrate de importar la función is_usql
from parser import is_usql, parser, translate_query


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
    # Prueba para cada consulta SQL a USQL

        # Prueba de SELECT con TODO
    def test_sql_to_usql_select_all(self):
        query = "SELECT * FROM usuarios WHERE edad > 18;"
        expected_output = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        self.run_query_test(query, expected_output)

    # Prueba de SELECT con DISTINCT
    def test_sql_to_usql_select_distinct(self):
        query = "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid';"
        expected_output = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"
        self.run_query_test(query, expected_output)

    # Prueba de INSERT
    def test_sql_to_usql_insert(self):
        query = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);"
        expected_output = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        self.run_query_test(query, expected_output)

    # Prueba de UPDATE
    def test_sql_to_usql_update(self):
        query = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero';"
        expected_output = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        self.run_query_test(query, expected_output)

    # Prueba de JOIN
    def test_sql_to_usql_join(self):
        query = "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona';"
        expected_output = "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';"
        self.run_query_test(query, expected_output)

    # Prueba de GROUP BY y COUNT
    def test_sql_to_usql_group_by_count(self):
        query = "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;"
        expected_output = "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;"
        self.run_query_test(query, expected_output)

    # Prueba de DELETE
    def test_sql_to_usql_delete(self):
        query = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25;"
        expected_output = "BORRA DE LA clientes DONDE edad ENTRE 18 Y 25;"
        self.run_query_test(query, expected_output)

    # Prueba de ALTER TABLE para agregar columna
    def test_sql_to_usql_alter_add_column(self):
        query = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;"
        expected_output = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;"
        self.run_query_test(query, expected_output)

    # Prueba de ALTER TABLE para eliminar columna
    def test_sql_to_usql_alter_drop_column(self):
        query = "ALTER TABLE empleados DROP COLUMN direccion;"
        expected_output = "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
        self.run_query_test(query, expected_output)

     # Pruebas para completar la cobertura

    # Prueba para `p_nullable`
    def test_nullable_no_nulo(self):
        query = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;"
        expected_output = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;"
        self.run_query_test(query, expected_output)

    # Prueba para `p_set_list`
    def test_set_list(self):
        query = "ACTUALIZA empleados SETEA salario = 3000, puesto = 'ingeniero' DONDE id = 1;"
        expected_output = "UPDATE empleados SET salario = 3000, puesto = 'ingeniero' WHERE id = 1;"
        self.run_query_test(query, expected_output)

    # Prueba para `p_select_elements` con `TODO`
    def test_select_elements_todo(self):
        query = "TRAEME TODO DE LA TABLA empleados;"
        expected_output = "SELECT * FROM empleados;"
        self.run_query_test(query, expected_output)

    # Prueba para `p_select_list`
    def test_select_list(self):
        query = "TRAEME nombre, edad DE LA TABLA usuarios;"
        expected_output = "SELECT nombre, edad FROM usuarios;"
        self.run_query_test(query, expected_output)

    # Prueba para `p_optional_usql_group_by`
    def test_optional_usql_group_by(self):
        query = "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;"
        expected_output = "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;"
        self.run_query_test(query, expected_output)

    # Prueba para `p_group_list`
    def test_group_list(self):
        query = "TRAEME nombre, edad DE LA TABLA clientes AGRUPANDO POR nombre;"
        expected_output = "SELECT nombre, edad FROM clientes GROUP BY nombre;"
        self.run_query_test(query, expected_output)

    # Prueba para `p_condition` con `BETWEEN`
    def test_condition_between(self):
        query = "BORRA DE LA clientes DONDE edad ENTRE 18 Y 25;"
        expected_output = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25;"
        self.run_query_test(query, expected_output)

    # Prueba para `p_error`
    def test_syntax_error(self):
        query = "TRAEME * FROM usuarios"
        with self.assertRaises(SyntaxError):
            self.run_query_test(query, None)

    # Prueba para `translate_query` de SQL a USQL
    def test_translate_sql_to_usql(self):
        query = "SELECT * FROM usuarios WHERE edad > 18;"
        expected_output = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        self.run_query_test(query, expected_output)


# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
