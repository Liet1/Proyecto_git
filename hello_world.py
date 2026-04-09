import http.server
import socketserver

PORT = 8000

html_content = b"""
<!DOCTYPE html>
<html>
<head>
    <title>Hello World Frontend</title>
</head>
<body>
    <h1>Cambio de prueba</h1>
    <p>Este es un ejemplo sencillo de frontend en Python.</p>
</body>
</html>
"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content)

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Sirviendo en el puerto {PORT}...")
        httpd.serve_forever()
