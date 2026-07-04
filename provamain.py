from provadatabase import criar_database
from http.server import HTTPServer
from routesprova import GerenciadorHandler

def main(): #fluxo da main pra recorrer as funcoes dos outros codigos secundarios
    criar_database() #a main precisa se responsabilizar de criar o db
    #o routes que vai usar asoutras funcoes do db ja criado pela main
    servidor = HTTPServer(("localhost", 8000), GerenciadorHandler) #chama o routes, que tem a parte web e as funcoes do database
    print(f'Servidor rodando em http://localhost:8000.')
    servidor.serve_forever() #so desliga o server se eu decidir, nao em x interações
    
if __name__ == "__main__": #ativacao da funcao main
    main()