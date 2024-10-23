import pytest
from dsl_usql import translate


def test_translation():
    assert translate(
        "SELECT * FROM usuarios WHERE edad > 18") == "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18"
    assert translate(
        "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18") == "SELECT * FROM usuarios WHERE edad > 18"

    assert translate(
        "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid'") == "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid'"

    assert translate(
        "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25)") == "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)"

    assert translate(
        "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero'") == "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero'"

    assert translate("TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona'") == \
        "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona'"

    assert translate("TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5") == \
        "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5"

    assert translate(
        "BORRA DE LA tabla clientes DONDE edad ENTRE 18 Y 25") == "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25"

    assert translate("CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO") == \
        "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL"

    assert translate("CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion") == \
        "ALTER TABLE empleados DROP COLUMN direccion"


# Ejecutar pruebas con pytest
pytest.main()
