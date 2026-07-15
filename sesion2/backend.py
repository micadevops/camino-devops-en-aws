from flask import Flask, request, jsonify
from datetime import datetime
import urllib.request
import os

from dotenv import load_dotenv
load_dotenv()

PORT = int(os.getenv('PORT', 5000))
NOMBRE_DEFAULT = os.getenv('NOMBRE', 'Desconocida')

app = Flask(__name__)

def get_az():
    try:
        return urllib.request.urlopen(
            'http://169.254.169.254/latest/meta-data/placement/availability-zone',
            timeout=2
        ).read().decode()
    except Exception:
        return 'local'

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/info')
def info():
    nombre = request.args.get('nombre', '').strip() or NOMBRE_DEFAULT
    az = get_az()
    fecha = datetime.now().strftime('%d/%m/%Y · %H:%M hs')
    return jsonify({'nombre': nombre, 'az': az, 'fecha': fecha})

if __name__ == '__main__':
    print(f'Backend corriendo en http://0.0.0.0:{PORT}')
    print(f'Nombre por defecto (desde .env): {NOMBRE_DEFAULT}')
    app.run(host='0.0.0.0', port=PORT)