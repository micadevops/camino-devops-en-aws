from flask import Flask, request, jsonify
from datetime import datetime
import urllib.request
import socket

PORT = 5000

app = Flask(__name__)

def get_az():
    try:
        token_req = urllib.request.Request(
            'http://169.254.169.254/latest/api/token',
            method='PUT',
            headers={'X-aws-ec2-metadata-token-ttl-seconds': '21600'}
        )
        token = urllib.request.urlopen(token_req, timeout=2).read().decode()
        az_req = urllib.request.Request(
            'http://169.254.169.254/latest/meta-data/placement/availability-zone',
            headers={'X-aws-ec2-metadata-token': token}
        )
        return urllib.request.urlopen(az_req, timeout=2).read().decode()
    except Exception:
        return 'local'

@app.after_request
def add_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/info')
def info():
    nombre = request.args.get('nombre', 'Desconocida').strip() or 'Desconocida'
    az = get_az()
    fecha = datetime.now().strftime('%d/%m/%Y · %H:%M hs')
    return jsonify({'nombre': nombre, 'az': az, 'fecha': fecha, 'pod': socket.gethostname()})

if __name__ == '__main__':
    print(f'Backend corriendo en http://0.0.0.0:{PORT}')
    app.run(host='0.0.0.0', port=PORT)