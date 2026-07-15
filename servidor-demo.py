from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"""
            <h1>Hola desde el servidor!</h1>
            <p>Este proceso esta escuchando en el puerto 3000.</p>
        """)

    def log_message(self, format, *args):
        print(f"  peticion recibida: {args[0]}")

print("archivo cargado en memoria, proceso iniciado")
print("escuchando en http://localhost:3000")
print("(Ctrl+C para detener)\n")

HTTPServer(("localhost", 3000), Handler).serve_forever()
