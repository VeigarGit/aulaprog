from http.server import BaseHTTPRequestHandler
from database import listar_tarefas
class GerenciadorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        tarefas = listar_tarefas()
        linhas_html = ""
        for tarefa in tarefas:
            linhas_html += f"<li>{tarefa['titulo']} - {tarefa['status']}</li>"
        html = f"<h1> minhas tarefas </h1><ul>{linhas_html}</ul>"
        


        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<h1> oi! </h1>".encode("utf-8"))