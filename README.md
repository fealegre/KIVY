# Kivy Lab

Proyecto educativo en Python para aprender a crear interfaces gráficas con Kivy mediante ejemplos prácticos, ejercicios y pequeños proyectos.

## Qué contiene este repositorio

El proyecto está organizado en carpetas temáticas para avanzar de forma progresiva:

- [basicos](basicos): introducción a widgets como botones, labels, inputs, checkboxes, sliders y spinners.
- [callbacks](callbacks): ejemplos de interacción y manejo de eventos.
- [layouts](layouts): uso de diferentes disposiciones visuales como BoxLayout, GridLayout y FloatLayout.
- [ejercicio_practica_primer_parcial](ejercicio_practica_primer_parcial): mini aplicaciones de práctica con lógica simple.
- [almacenamientos](almacenamientos): ejemplos de lectura/escritura de archivos, almacenamiento en SQLite y uso de JSON para guardar preferencias.

## Enfoque del proyecto

Este repositorio busca enseñar Kivy de forma práctica, empezando por los conceptos básicos y avanzando hacia aplicaciones más completas. Cada ejemplo está pensado para ser ejecutado por separado y comprender cómo se construye una interfaz gráfica paso a paso.

## Ejemplos incluidos

### Básicos
- [basicos/hello.py](basicos/hello.py): primera app con un mensaje simple.
- [basicos/buttons.py](basicos/buttons.py): botones y organización básica de la interfaz.
- [basicos/text_inputs.py](basicos/text_inputs.py): entrada de texto.
- [basicos/checkboxes.py](basicos/checkboxes.py): casillas de selección.
- [basicos/sliders.py](basicos/sliders.py): barras deslizantes.
- [basicos/spinners.py](basicos/spinners.py): listas desplegables.

### Interacción y layouts
- [callbacks/button_callbacks.py](callbacks/button_callbacks.py): eventos y callbacks.
- [layouts/box_layout_h.py](layouts/box_layout_h.py): distribución horizontal.
- [layouts/grid_layout.py](layouts/grid_layout.py): diseño tipo grilla.
- [layouts/float_layout.py](layouts/float_layout.py): posicionamiento libre.

### Práctica
- [ejercicio_practica_primer_parcial/saludo_interactivo.py](ejercicio_practica_primer_parcial/saludo_interactivo.py): app que saluda al usuario.
- [ejercicio_practica_primer_parcial/contador_clicks.py](ejercicio_practica_primer_parcial/contador_clicks.py): contador de clics.
- [ejercicio_practica_primer_parcial/calculadora_basica.py](ejercicio_practica_primer_parcial/calculadora_basica.py): calculadora simple.
- [ejercicio_practica_primer_parcial/conversor_temperaturas.py](ejercicio_practica_primer_parcial/conversor_temperaturas.py): conversor de temperaturas.

### Almacenamiento
- [almacenamientos/archivos.py](almacenamientos/archivos.py): manejo de archivos de texto.
- [almacenamientos/bd.py](almacenamientos/bd.py): ejemplo básico con SQLite.
- [almacenamientos/preferencias.py](almacenamientos/preferencias.py): guardar y cargar preferencias en JSON.
- [almacenamientos/integracion_minima_SQL.py](almacenamientos/integracion_minima_SQL.py): app de agenda con interfaz mejorada y base de datos.
- [almacenamientos/integracion_minima_JSON.py](almacenamientos/integracion_minima_JSON.py): ejemplo simple de guardado en JSON.

## Requisitos

- Python 3.9 o superior
- Kivy

Instala Kivy con:

```bash
pip install kivy
```

## Cómo ejecutar un ejemplo

Por ejemplo:

```bash
python basicos/hello.py
```

O una app más completa:

```bash
python "almacenamientos/integracion_minima_SQL.py"
```

## Objetivo

Aprender a construir interfaces gráficas con Python y Kivy, integrar lógica de negocio simple y trabajar con almacenamiento local de forma práctica.

## Autor

Fernando Alegre
