import sqlite3

conn = sqlite3.connect("datos.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    estado TEXT NOT NULL
)
""")

cur.execute(
    "INSERT INTO tareas (titulo, estado) VALUES (?, ?)", ("Estudiar Kivy", "pendiente")
)
conn.commit()

for fila in cur.execute("SELECT id, titulo, estado FROM tareas"):
    print(fila)

conn.close()
