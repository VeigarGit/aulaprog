# ==================== BIBLIOTECA (Library) ====================
# Você controla o fluxo. A biblioteca te ajuda.
import random

numeros = [1, 2, 3, 4, 5]
escolhido = random.choice(numeros)
print(f"Número sorteado: {escolhido}")


# ==================== FRAMEWORK ====================
# O framework controla o fluxo (Inversão de Controle).
# Exemplo com Flask (você só define as rotas):

"""
from http.server import HTTPServer, BaseHTTPRequestHandler

class MeuHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Olá, mundo!".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Página não encontrada".encode("utf-8"))

servidor = HTTPServer(("localhost", 5000), MeuHandler)

print("Servidor rodando em http://localhost:5000")
servidor.serve_forever()
"""
