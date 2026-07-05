from http.server import HTTPServer 
from routes import GerenciadorHandler
from database import create_tables

def main():
    create_tables()
    server = HTTPServer(('localhost', 8000), GerenciadorHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()

