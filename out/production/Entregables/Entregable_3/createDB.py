import sqlite3


def create_database(db_path):
    """Creates an SQLite database with example tables and data for testing."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create tables if they do not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER,
            email TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            ciudad TEXT,
            edad INTEGER
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            puesto TEXT,
            salario INTEGER,
            direccion TEXT
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            producto TEXT,
            cantidad INTEGER,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT,
            cantidad INTEGER
        );
    ''')

    # Insert sample data
    cursor.executemany("INSERT INTO usuarios (nombre, edad, email) VALUES (?, ?, ?)", [
        ('Juan Pérez', 25, 'juan.perez@example.com'),
        ('Ana Gómez', 30, 'ana.gomez@example.com'),
        ('Luis Torres', 17, 'luis.torres@example.com')
    ])
    cursor.executemany("INSERT INTO clientes (nombre, ciudad, edad) VALUES (?, ?, ?)", [
        ('Carlos Ruiz', 'Madrid', 22),
        ('Maria López', 'Barcelona', 29),
        ('Jose Fernandez', 'Madrid', 18)
    ])
    cursor.executemany("INSERT INTO empleados (nombre, puesto, salario, direccion) VALUES (?, ?, ?, ?)", [
        ('Laura Martin', 'ingeniero', 2500, None),
        ('Andres Ruiz', 'analista', 2000, None)
    ])
    cursor.executemany("INSERT INTO pedidos (cliente_id, producto, cantidad) VALUES (?, ?, ?)", [
        (1, 'Producto A', 2),
        (2, 'Producto B', 3),
        (3, 'Producto C', 1)
    ])
    cursor.executemany("INSERT INTO ventas (producto, cantidad) VALUES (?, ?)", [
        ('Producto A', 5),
        ('Producto B', 3),
        ('Producto C', 7)
    ])

    # Confirm changes and close connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Database created and populated with initial data.")


# Create the database
db_path = "mi_base_de_datos.db"
create_database(db_path)
