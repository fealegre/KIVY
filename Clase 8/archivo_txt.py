from pathlib import Path

archivo = Path("notas.txt")

with archivo.open("a", encoding="utf-8") as f:
    f.write("Primera nota\n")

contenido = archivo.read_text(encoding="utf-8")
print(contenido)


