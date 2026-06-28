# Maneja la lectura y escritura de un archivo de texto sencillo.
from pathlib import Path

archivos = Path(__file__).parent / "notas.txt"

texto_lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

with archivos.open("a") as archivo:
    archivo.write(texto_lorem)

content = archivos.read_text()
print(content)
