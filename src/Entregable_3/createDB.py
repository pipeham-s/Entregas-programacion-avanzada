import sqlite3

def create_database(db_path):
    """Crea una base de datos SQLite y una tabla de ejemplo si no existe."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Crear la tabla de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER,
            email TEXT
        );
    ''')
    
    # Insertar datos de ejemplo
    cursor.execute("INSERT INTO usuarios (nombre, edad, email) VALUES ('Juan Pérez', 25, 'juan.perez@example.com')")
    cursor.execute("INSERT INTO usuarios (nombre, edad, email) VALUES ('Ana Gómez', 30, 'ana.gomez@example.com')")
    cursor.execute("INSERT INTO usuarios (nombre, edad, email) VALUES ('Luis Torres', 17, 'luis.torres@example.com')")
    
    # Confirmar cambios y cerrar conexión
    conn.commit()
    cursor.close()
    conn.close()
    print("Base de datos creada y datos insertados.")

# Crear la base de datos
db_path = "mi_base_de_datos.db"
create_database(db_path)
