from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Sesion 3 - De Cero a Cloud en AWS</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                background: linear-gradient(135deg, #070A1A 0%, #1a1040 50%, #7C3AED 100%);
                font-family: -apple-system, 'Segoe UI', system-ui, sans-serif;
                color: white;
            }
            .card {
                text-align: center;
                padding: 60px 50px;
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 20px;
                backdrop-filter: blur(10px);
                max-width: 520px;
            }
            .emoji { font-size: 60px; margin-bottom: 20px; }
            h1 { font-size: 28px; font-weight: 800; margin-bottom: 8px; }
            .purple { color: #C4B5FD; }
            .sub { color: rgba(255,255,255,0.6); font-size: 15px; margin-bottom: 24px; }
            .badge {
                display: inline-block;
                background: #7C3AED;
                padding: 6px 18px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: 700;
                letter-spacing: 0.1em;
                text-transform: uppercase;
            }
            .footer { margin-top: 30px; font-size: 13px; color: rgba(255,255,255,0.4); }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="emoji">&#x1F680;</div>
            <h1>Bienvenidas a la <span class="purple">Sesion 3</span></h1>
            <p class="sub">De Cero a Cloud: El camino DevOps en AWS</p>
            <span class="badge">Corriendo en Docker</span>
            <p class="footer">AWS Girls UG Uruguay</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok", "session": 3}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
