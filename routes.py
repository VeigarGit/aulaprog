from http.server import BaseHTTPRequestHandler
from database import listar_tarefas, inserir_tarefas
from datetime import datetime
from urllib.parse import parse_qs
class GerenciadorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        tarefas = listar_tarefas()
        linhas_html = ""
        for tarefa in tarefas:
            linhas_html += f"<li>{tarefa['titulo']} - {tarefa['status']}</li>"
        html = f"""<h1> minhas tarefas </h1> <ul>{linhas_html}</ul>

        <form method="POST" action="/adicionar">
            <input type="text" name="titulo" placeholder="Título">
            <input type="text" name="descricao" placeholder="Descrição">
            <button type="submit">Adicionar</button>
        </form>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


    def do_POST(self):
        tamanho = int(self.headers["Content-Length"])
        corpo = self.rfile.read(tamanho).decode("utf-8")
        dados = parse_qs(corpo)
        titulo = dados["titulo"][0]
        descricao = dados["descricao"][0]
        inserir_tarefas(titulo,descricao,datetime.now(), None, None)
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()


        