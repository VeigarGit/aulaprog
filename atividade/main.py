from http.server import HTTPServer
from routes import MeuHandler
import database

if __name__ == "__main__":
    database.criar_tabelas()
    servidor = HTTPServer(("localhost", 5000), MeuHandler)
    print("Servidor rodando em http://localhost:5000")
    servidor.serve_forever()