# Crea y popula una base de datos SQLite básica con ejemplos de tareas.
import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path(__file__).parent / "database.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")

cursor.execute("""INSERT INTO tareas (titulo, descripcion) VALUES
    ('Comprar víveres', 'Comprar leche, pan y huevos'),
    ('Llamar al médico', 'Agendar cita para revisión anual'),
    ('Estudiar para el examen', 'Repasar los capítulos 1 a 5 del libro de texto')
""")

conn.commit()
conn.close()
