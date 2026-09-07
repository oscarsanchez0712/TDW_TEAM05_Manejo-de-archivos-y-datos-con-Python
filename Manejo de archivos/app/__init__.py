import os
import json
from collections import Counter
from datetime import datetime
from flask import Flask, render_template, request, jsonify


def create_app():
    app = Flask(__name__)
    data_file = os.path.join(app.root_path, "datos.json")

    def leer_datos():
        if not os.path.exists(data_file):
            return []
        with open(data_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def guardar_datos(datos):
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/subir", methods=["POST"])
    def subir_archivo():
        archivo = request.files.get("archivo")
        if not archivo or archivo.filename == "":
            return jsonify({"error": "No se seleccionó ningún archivo"}), 400

        contenido = archivo.read().decode("utf-8", errors="ignore")

        palabras = contenido.split()
        frecuencia = Counter(palabras)
        mas_comun = frecuencia.most_common(1)[0][0] if frecuencia else "-"

        registro = {
            "nombre": archivo.filename,
            "lineas": contenido.count("\n") + 1,
            "palabras": len(palabras),
            "caracteres": len(contenido),
            "palabra_frecuente": mas_comun,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        datos = leer_datos()
        datos.append(registro)
        guardar_datos(datos)

        return jsonify({**registro, "contenido": contenido})

    @app.route("/historial")
    def historial():
        return jsonify(leer_datos())

    return app
