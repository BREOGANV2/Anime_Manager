from flask import Flask, render_template, request, jsonify
import json
import os
import threading
import webbrowser

app = Flask(__name__)
SEEN_FILE = "seen_animes.json"

def cargar_vistos():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE, 'r') as f:
            return json.load(f)
    return []

def guardar_vistos(lista):
    with open(SEEN_FILE, 'w') as f:
        json.dump(lista, f)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/seen', methods=['GET', 'POST'])
def api_seen():
    if request.method == 'GET':
        return jsonify(cargar_vistos())
    if request.method == 'POST':
        data = request.json
        guardar_vistos(data.get("seen", []))
        return jsonify({"status": "ok"})

def abrir_navegador():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    threading.Timer(1, abrir_navegador).start()
    app.run(debug=True)
