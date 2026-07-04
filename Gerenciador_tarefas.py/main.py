from http.server import HTTPServer
from rotas import GerenciadorTarefas
import database

if __name__ == "__main__":
    database.init_db()  
    servidor = HTTPServer(("localhost", 5000), GerenciadorTarefas)
    
    print("Servidor rodando em http://localhost:5000")
    print("Pressione CTRL+C para encerrar o servidor no terminal.")
    
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")