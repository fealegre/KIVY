# Guarda y carga preferencias en formato JSON desde un archivo de configuración.
import json
from pathlib import Path

CONFIG = Path(__file__).parent / "config.json"


def guardar_preferencias(preferencias):
    CONFIG.write_text(json.dumps(preferencias, indent=4))


def cargar_preferencias():
    if CONFIG.exists():
        return json.loads(CONFIG.read_text())
    else:
        return {}


if __name__ == "__main__":
    # Ejemplo de uso
    preferencias = {"tema": "claro", "idioma": "en", "notificaciones": False}
    guardar_preferencias(preferencias)
    print("Preferencias guardadas.")

    preferencias_cargadas = cargar_preferencias()
    print("Preferencias cargadas:", preferencias_cargadas)
