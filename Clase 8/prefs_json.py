import json
from pathlib import Path

CONFIG = Path("config.json")

def guardar_preferencias(datos):
    CONFIG.write_text(json.dumps(datos, indent=2), encoding="utf-8")

def cargar_preferencias():
    if CONFIG.exists():
        return json.loads(CONFIG.read_text(encoding="utf-8"))
    return {"tema": "claro", "idioma": "es"}

prefs = cargar_preferencias()
prefs["tema"] = "oscuro"
guardar_preferencias(prefs)

