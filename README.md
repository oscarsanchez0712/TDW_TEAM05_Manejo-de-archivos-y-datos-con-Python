# 📂 Manejo de archivos y datos con Python

Proyecto realizado con **Python + Flask** para demostrar el manejo, lectura, escritura y análisis de archivos y datos.

La aplicación permite seleccionar un archivo, subirlo y analizar su contenido, mostrando información como:

* 📄 Nombre del archivo
* 📏 Cantidad de líneas
* 🔤 Cantidad de palabras
* 🔢 Cantidad de caracteres
* ⭐ Palabra más frecuente
* 🕘 Historial de archivos analizados

---

## 🛠️ Tecnologías utilizadas

* Python
* Flask
* HTML5
* CSS3
* JavaScript
* JSON
* Tailwind CSS

---

## 📁 Estructura del proyecto

```text
Manejo de archivos/
│
├── app/
│   ├── routes/
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── input.css
│   │   │   ├── output.css
│   │   │   └── style.css
│   │   │
│   │   ├── img/
│   │   │
│   │   └── js/
│   │       └── style.js
│   │
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   │
│   ├── __init__.py
│   └── datos.json
│
├── venv/
│
├── app.py
├── package.json
├── package-lock.json
├── requirements.txt
├── tailwind.config.js
└── README.md
```

---

# 🚀 Instalación

## 1. Crear el entorno virtual

Desde la terminal de VS Code:

```bash
py -m venv venv
```

Este comando crea un entorno virtual llamado `venv`.

---

## 2. Activar el entorno virtual

En Windows PowerShell:

```powershell
venv\Scripts\activate
```

Si se activó correctamente, aparecerá algo parecido a:

```text
(venv) PS C:\Users\sanch\Desktop\Manejo de archivos>
```

---

## 3. Instalar Flask

Con el entorno virtual activado:

```bash
pip install flask
```

También se pueden instalar todas las dependencias utilizando:

```bash
pip install -r requirements.txt
```

---

# 📦 requirements.txt

El archivo `requirements.txt` contiene las dependencias necesarias para ejecutar el proyecto.

Ejemplo:

```text
Flask
```

Para generar automáticamente el archivo con las librerías instaladas:

```bash
pip freeze > requirements.txt
```

---

# 🐍 Código principal de Python

El archivo principal del proyecto es:

```text
app.py
```

Un ejemplo básico para iniciar Flask es:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Hola, Flask"

if __name__ == "__main__":
    app.run(debug=True)
```

---

# 📂 Manejo de archivos

Python permite trabajar con archivos utilizando la función `open()`.

## Leer un archivo

```python
with open("archivo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print(contenido)
```

## Escribir en un archivo

```python
with open("archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola desde Python")
```

## Agregar información

```python
with open("archivo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("\nNueva información")
```

---

# 📊 Análisis del archivo

Una vez obtenido el contenido del archivo, podemos analizar sus datos.

## Contar caracteres

```python
caracteres = len(contenido)
```

## Contar líneas

```python
lineas = len(contenido.splitlines())
```

## Contar palabras

```python
palabras = contenido.split()
cantidad_palabras = len(palabras)
```

---

# ⭐ Encontrar la palabra más frecuente

Python permite utilizar `Counter` para determinar cuántas veces aparece cada palabra.

```python
from collections import Counter

palabras = contenido.lower().split()

contador = Counter(palabras)

palabra_mas_frecuente = contador.most_common(1)[0][0]
```

Por ejemplo, si el texto contiene:

```text
Python es fácil.
Python es poderoso.
Python es popular.
```

El resultado sería:

```text
Palabra más frecuente: python
```

---

# 🌐 Subir archivos con Flask

Flask permite recibir archivos enviados desde un formulario HTML.

Ejemplo:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    resultado = None

    if request.method == "POST":

        archivo = request.files["archivo"]

        if archivo:

            contenido = archivo.read().decode("utf-8")

            resultado = {
                "nombre": archivo.filename,
                "lineas": len(contenido.splitlines()),
                "palabras": len(contenido.split()),
                "caracteres": len(contenido)
            }

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🖥️ HTML

El formulario se encuentra en:

```text
app/templates/index.html
```

Ejemplo:

```html
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Manejo de archivos</title>
</head>

<body>

    <h1>Manejo de archivos y datos con Python</h1>

    <p>Demo con Flask</p>

    <form method="POST" enctype="multipart/form-data">

        <input type="file" name="archivo" required>

        <button type="submit">
            Subir y analizar archivo
        </button>

    </form>

</body>

</html>
```

El atributo:

```html
enctype="multipart/form-data"
```

es necesario para poder enviar archivos desde el formulario hacia el servidor.

---

# 💾 Manejo de datos con JSON

El proyecto también utiliza `datos.json` para almacenar información de los archivos analizados.

Ejemplo:

```json
[
    {
        "archivo": "guion-proyecto-html5.md",
        "lineas": 126,
        "palabras": 1035,
        "fecha": "2026-09-06 21:29:37"
    }
]
```

---

# 📖 Leer datos desde JSON

En Python podemos leer el archivo JSON utilizando el módulo `json`.

```python
import json

with open("app/datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print(datos)
```

---

# ✏️ Guardar datos en JSON

Para guardar información en `datos.json`:

```python
import json

datos = []

nuevo_dato = {
    "archivo": "ejemplo.txt",
    "lineas": 10,
    "palabras": 100,
    "caracteres": 500
}

datos.append(nuevo_dato)

with open("app/datos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
```

---

# ▶️ Ejecutar el proyecto

Primero debemos activar el entorno virtual:

```powershell
venv\Scripts\activate
```

Luego ejecutamos la aplicación:

```bash
python app.py
```

También podemos utilizar:

```bash
flask run
```

Al ejecutar Flask aparecerá una dirección similar a:

```text
http://127.0.0.1:5000
```

Abrimos esta dirección en el navegador para acceder a la aplicación.

---

# 📸 Resultado

La aplicación muestra una interfaz donde el usuario puede seleccionar un archivo y analizar su contenido.

El resultado incluye información como:

```text
Archivo: guion-proyecto-html5.md

Líneas: 126
Palabras: 1035
Caracteres: 6982

Palabra más frecuente: de
```

También se muestra un **historial de los archivos procesados**, almacenado mediante JSON.

---

# 🎯 Objetivo del proyecto

El objetivo principal del proyecto es demostrar el manejo de archivos y datos utilizando Python y Flask.

Durante el desarrollo se aplican los siguientes conceptos:

* Creación de entornos virtuales.
* Instalación de paquetes mediante `pip`.
* Desarrollo de aplicaciones web con Flask.
* Lectura y escritura de archivos.
* Procesamiento de texto.
* Conteo de líneas, palabras y caracteres.
* Uso de `Counter`.
* Manejo de archivos enviados desde HTML.
* Lectura y escritura de archivos JSON.
* Uso de plantillas HTML.
* Separación entre backend y frontend.

---

# 💻 Comandos utilizados

### Crear entorno virtual

```bash
py -m venv venv
```

### Activar entorno virtual

```powershell
venv\Scripts\activate
```

### Instalar Flask

```bash
pip install flask
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Generar requirements.txt

```bash
pip freeze > requirements.txt
```

### Ejecutar la aplicación

```bash
python app.py
```

### Ejecutar Flask

```bash
flask run
```

### Desactivar el entorno virtual

```bash
deactivate
```

---

# 📌 Conclusión

El proyecto permite comprender de manera práctica cómo Python puede utilizarse para trabajar con archivos y datos. Mediante Flask se desarrolló una aplicación web capaz de recibir archivos, analizar su contenido y almacenar un historial de resultados utilizando archivos JSON.

De esta manera, se integran conceptos de **Python, Flask, HTML, CSS, JavaScript y JSON**, demostrando el funcionamiento básico de una aplicación web para el procesamiento de información.
