# Manejo de archivos y datos con Python

Demo académica con Flask, Tailwind y JavaScript. Permite subir un archivo de texto,
analizarlo (líneas, palabras, palabra más frecuente) y ver su contenido completo,
además de un historial de archivos procesados.

## Estructura

```
demo_python_archivos/
├── app/
│   ├── __init__.py       # fábrica de la app Flask
│   ├── routes/           # rutas: /, /subir, /historial
│   ├── static/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   └── templates/
├── app.py                # punto de entrada
├── requirements.txt
└── tailwind.config.js
```

## Cómo correrlo

```bash
pip install -r requirements.txt
python app.py
```

Abre `http://localhost:5000`.
