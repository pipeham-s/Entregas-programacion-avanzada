# Importe del lexer y parser desde el archivo donde tienes definido tu DSL
# Asumiendo que tu archivo se llama dsl_usql.py
from dsl_usql import translate

# Función de prueba


def run_test(query, expected_output):
    result = translate(query)
    if result == expected_output:
        print(f"PASSED: {query} => {result}")
    else:
        print(f"FAILED: {query} => {result} (Expected: {expected_output})")


# Pruebas con consultas SQL y su equivalente USQL
tests = [
    ("SELECT * FROM usuarios WHERE edad > 18",
     "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18"),
    ("TRAEME TODO DE LA TABLA usuarios DONDE edad > 18",
     "SELECT * FROM usuarios WHERE edad > 18"),
    ("INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)",
     "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25)"),
    ("METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25)",
     "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)"),
    ("UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero'",
     "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero'"),
    ("ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero'",
     "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero'"),
    ("DELETE FROM clientes WHERE edad BETWEEN 18 AND 25",
     "BORRA DE LA clientes DONDE edad ENTRE 18 Y 25"),
    ("BORRA DE LA clientes DONDE edad ENTRE 18 Y 25",
     "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25")
]

# Ejecutar las pruebas
for test in tests:
    run_test(*test)

query = "SELECT * FROM usuarios WHERE edad > 18"
result = translate(query)
print(result)
