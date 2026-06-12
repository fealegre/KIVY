# 🧪 Kivy Lab

<div align="center">

![Kivy](https://img.shields.io/badge/Kivy-2.x-FF6600?style=for-the-badge&logo=kivy&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

**✨ Un laboratorio interactivo para explorar y dominar el framework Kivy desde cero ✨**

</div>

---

## 🚀 ¿Qué es esto?

**Kivy Lab** es una colección progresiva de ejemplos prácticos que te guiarán a través de los fundamentos de **Kivy**, el framework de Python para crear interfaces gráficas multiplataforma (Windows, macOS, Linux, Android, iOS).

Cada archivo es una pieza de aprendizaje independiente, diseñada para ser leída y ejecutada por separado, con comentarios didácticos que explican _qué_ hace cada línea y _por qué_ funciona así.

---

## 🗺️ Mapa de aprendizaje

```
📦 KIVY LAB
├── 🟢 NIVEL 1 — Fundamentos
│   ├── hello.py              → Tu primera app: "Hola, Mundo!"
│   ├── text_inputs.py        → Campos de texto con placeholder
│   └── buttons.py            → Botones en layout vertical
│
├── 🟡 NIVEL 2 — Interacción
│   ├── checkboxes.py         → Casillas de verificación
│   ├── sliders.py            → Barra deslizante y eventos en vivo
│   └── spinners.py           → Lista desplegable (select)
│
├── 🔵 NIVEL 3 — Eventos y Callbacks
│   └── callbacks/
│       └── button_callbacks.py → Cómo enlazar eventos a funciones
│
├── 🟣 NIVEL 4 — Layouts (Disposición)
│   ├── layouts/box_layout_h.py → Disposición horizontal
│   ├── layouts/grid_layout.py  → Cuadrícula tipo tabla
│   └── layouts/float_layout.py → Posicionamiento libre y preciso
│
└── 🏆 NIVEL 5 — Proyectos prácticos
    └── ejercicio_practica_parcial/
        ├── saludo_interactivo.py → App que saluda al usuario
        ├── contador_clicks.py    → Contador con colores dinámicos
        └── calculadora_basica.py → Calculadora con validaciones
```

---

## 🧠 Conceptos que aprenderás

### 🟢 Nivel 1 — Fundamentos

| Concepto                                                   | Archivo          |
| ---------------------------------------------------------- | ---------------- |
| `App`, `Label`, `build()`                                  | `hello.py`       |
| `TextInput`, `hint_text`, `multiline`                      | `text_inputs.py` |
| `Button`, `BoxLayout`, `orientation`, `padding`, `spacing` | `buttons.py`     |

### 🟡 Nivel 2 — Interacción

| Concepto                                            | Archivo         |
| --------------------------------------------------- | --------------- |
| `CheckBox`, `texture_update()`, `Window.clearcolor` | `checkboxes.py` |
| `Slider`, `bind()`, callbacks de propiedad          | `sliders.py`    |
| `Spinner`, `values`, selección desplegable          | `spinners.py`   |

### 🔵 Nivel 3 — Eventos

| Concepto                              | Archivo                         |
| ------------------------------------- | ------------------------------- |
| `on_press`, `bind()`, `instance.text` | `callbacks/button_callbacks.py` |

### 🟣 Nivel 4 — Layouts

| Concepto                               | Archivo                   |
| -------------------------------------- | ------------------------- |
| `orientation="horizontal"`             | `layouts/box_layout_h.py` |
| `GridLayout`, `cols`, filas y columnas | `layouts/grid_layout.py`  |
| `FloatLayout`, `pos_hint`, `size_hint` | `layouts/float_layout.py` |

### 🏆 Nivel 5 — Proyectos

| Concepto                                                       | Archivo                                            |
| -------------------------------------------------------------- | -------------------------------------------------- |
| Widget personalizado, `bind()`, `strip()`                      | `ejercicio_practica_parcial/saludo_interactivo.py` |
| `NumericProperty`, patrón reactivo, colores dinámicos          | `ejercicio_practica_parcial/contador_clicks.py`    |
| Validación de entrada, manejo de errores, `GridLayout` anidado | `ejercicio_practica_parcial/calculadora_basica.py` |

---

## ⚡ Cómo empezar

### 1️⃣ Instalar Kivy

```bash
pip install kivy
```

> 🐍 Requiere Python 3.8 o superior.

### 2️⃣ Clonar el repositorio

```bash
git clone https://github.com/fealegre/KIVY.git
cd KIVY
```

### 3️⃣ Ejecutar cualquier ejemplo

```bash
python hello.py          # El clásico "Hola, Mundo!"
python buttons.py        # Botones interactivos
python sliders.py        # Deslizador en acción

# O los proyectos completos
python ejercicio_practica_parcial/saludo_interactivo.py
python ejercicio_practica_parcial/calculadora_basica.py
```

---

## 🧪 Ejecución rápida de todos los ejemplos

```bash
# Nivel 1
python hello.py && python text_inputs.py && python buttons.py

# Nivel 2
python checkboxes.py && python sliders.py && python spinners.py

# Nivel 3
python callbacks/button_callbacks.py

# Nivel 4
python layouts/box_layout_h.py
python layouts/grid_layout.py
python layouts/float_layout.py

# Nivel 5
python ejercicio_practica_parcial/saludo_interactivo.py
python ejercicio_practica_parcial/contador_clicks.py
```

---

## 🧩 Lo que hace único a este laboratorio

| Característica                     | Descripción                                               |
| ---------------------------------- | --------------------------------------------------------- |
| 📚 **Progresión natural**          | Cada archivo se construye sobre conceptos del anterior    |
| 💬 **Código comentado en español** | Explicaciones claras y detalladas línea por línea         |
| 🎯 **Ejemplos atómicos**           | Cada archivo es autónomo y ejecutable por sí mismo        |
| 🧪 **Proyectos reales**            | Ejercicios que integran múltiples conceptos               |
| 🎨 **UI atractiva**                | Colores, layouts y widgets bien diseñados desde el inicio |

---

## 📸 Vista previa de los proyectos

```
┌──────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐
│  ¡Hola, Fer! 👋      │   │        🟢             │   │  Calculadora          │
│                      │   │        42             │   │  ┌──────┐ ┌──────┐   │
│ [Escribe tu nombre]  │   │   Clics realizados    │   │  │  5   │ │  3   │   │
│ [    Saludar    ]    │   │  ┌──────┐ ┌────────┐  │   │  └──────┘ └──────┘   │
│                      │   │  │Sumar │ │Reinic. │  │   │ [+Sumar] [-Restar]   │
└──────────────────────┘   └──────────────────────┘   │ [*Mult.]  [/Dividir] │
   Saludo Interactivo            Contador              │  Resultado: 8        │
                                                        └──────────────────────┘
                                                             Calculadora
```

---

## 🛠️ Tecnologías

- **[Kivy](https://kivy.org/)** — Framework GUI multiplataforma de código abierto
- **Python 3** — Lenguaje de programación
- **Git** — Control de versiones

---

## 👨‍💻 Autor

**Fernando Alegre**

[![GitHub](https://img.shields.io/badge/GitHub-fealegre-181717?style=flat-square&logo=github)](https://github.com/fealegre)

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.  
Usa, modifica y comparte libremente.

---

<div align="center">

**Hecho con ❤️ y mucho ☕ para la comunidad Python 🐍**

</div>
