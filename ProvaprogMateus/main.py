from http.server import HTTPServer
import database
from server import TaskManagerHandler

HOST = "localhost"
PORT = 5000


def main():
    database.criar_tabelas()
    servidor = HTTPServer((HOST, PORT), TaskManagerHandler)
    print(f"Servidor rodando em http://{HOST}:{PORT}")
    servidor.serve_forever()


if __name__ == "__main__":
    main()
