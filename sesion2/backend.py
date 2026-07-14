from flask import Flask, request, Response
from datetime import datetime
import urllib.request
import os

from dotenv import load_dotenv
load_dotenv()

PORT  = int(os.getenv('PORT', 5000))
NOMBRE_DEFAULT = os.getenv('NOMBRE', 'Desconocida')

app = Flask(__name__)

TROPHY_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{nombre} · De Cero a Cloud</title>
  <style>
    *{{box-sizing:border-box;margin:0;padding:0}}
    body{{
      min-height:100vh;background:#050A14;
      background-image:radial-gradient(ellipse 60% 50% at 50% 0%,rgba(124,58,237,.18),transparent);
      display:flex;align-items:center;justify-content:center;
      font-family:-apple-system,'Segoe UI',system-ui,sans-serif;
    }}
    .card{{
      background:linear-gradient(160deg,#0F1432 0%,#080C1F 100%);
      border:1px solid rgba(124,58,237,.4);border-radius:24px;
      padding:52px 48px;width:100%;max-width:480px;text-align:center;
      animation:breathe 4s ease-in-out infinite;
    }}
    @keyframes breathe{{0%,100%{{box-shadow:0 0 40px rgba(124,58,237,.12)}}50%{{box-shadow:0 0 70px rgba(124,58,237,.28)}}}}
    .badge{{
      display:inline-block;font-size:11px;font-weight:700;letter-spacing:.12em;
      text-transform:uppercase;color:#9171F8;
      background:rgba(124,58,237,.15);border:1px solid rgba(124,58,237,.3);
      border-radius:20px;padding:5px 14px;margin-bottom:28px;
    }}
    .icon{{font-size:52px;margin-bottom:20px;}}
    .label{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.3);margin-bottom:8px;}}
    h1{{
      font-size:clamp(32px,8vw,52px);font-weight:800;color:#C4B5FD;
      text-shadow:0 0 40px rgba(167,139,250,.4);margin-bottom:6px;
    }}
    .sub{{font-size:14px;color:rgba(255,255,255,.4);margin-bottom:32px;}}
    .info-row{{display:flex;flex-direction:column;gap:8px;margin-bottom:32px;}}
    .info-item{{
      background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);
      border-radius:10px;padding:12px 16px;
      display:flex;justify-content:space-between;align-items:center;
    }}
    .info-key{{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.35);}}
    .info-val{{font-size:13px;font-weight:700;color:#fff;font-family:monospace;}}
    .hashtag{{font-size:13px;color:rgba(255,255,255,.25);letter-spacing:.04em;}}
    .hashtag span{{color:#7C3AED;}}
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">Deployado en AWS · EC2</div>
    <div class="icon">🚀</div>
    <div class="label">Primera vez en la nube</div>
    <h1>{nombre}</h1>
    <p class="sub">lanzó y configuró su primera instancia EC2</p>
    <div class="info-row">
      <div class="info-item">
        <span class="info-key">Availability Zone</span>
        <span class="info-val">{az}</span>
      </div>
      <div class="info-item">
        <span class="info-key">Deployado el</span>
        <span class="info-val">{fecha}</span>
      </div>
    </div>
    <p class="hashtag"><span>#DeCeroaCloud</span> · AWS Girls UG UY</p>
  </div>
</body>
</html>"""

def get_az():
    try:
        return urllib.request.urlopen(
            'http://169.254.169.254/latest/meta-data/placement/availability-zone',
            timeout=2
        ).read().decode()
    except Exception:
        return 'local'

@app.route('/trophy')
def trophy():
    # El nombre viene del form — si no hay, usa el del .env
    nombre = request.args.get('nombre', '').strip() or NOMBRE_DEFAULT
    az    = get_az()
    fecha = datetime.now().strftime('%d/%m/%Y · %H:%M hs')
    return Response(TROPHY_HTML.format(nombre=nombre, az=az, fecha=fecha), mimetype='text/html')

if __name__ == '__main__':
    print(f'Backend corriendo en http://0.0.0.0:{PORT}')
    print(f'Nombre por defecto (desde .env): {NOMBRE_DEFAULT}')
    app.run(host='0.0.0.0', port=PORT)