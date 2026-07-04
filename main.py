from http.server import HTTPServer
from routes import GerenciadorHandler
from database import criar_tabelas



def main():
    criar_tabelas()
    servidor = HTTPServer(("localhost", 8000), GerenciadorHandler)
    servidor.serve_forever()


if __name__ == "__main__":
    main()