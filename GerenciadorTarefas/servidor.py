from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader

import db

env = Environment(loader=FileSystemLoader("frontend"))


class TaskHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/":
            status = query.get("status", [None])[0]
            tarefas = db.listar_tarefas(status)
            html = env.get_template("index.html").render(
                tarefas=tarefas, filtro=status
            )
            self.mandar_pagina(html)

        elif path == "/editar":
            task_id = int(query["id"][0])
            tarefa = db.buscar_tarefa(task_id)
            if tarefa is None:
                self.send_response(404)
                self.end_headers()
                return
            html = env.get_template("edit.html").render(tarefa=tarefa)
            self.mandar_pagina(html)

        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode() if content_length else ""
        data = parse_qs(body)
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/adicionar":
            titulo = data.get("titulo", [""])[0]
            descricao = data.get("descricao", [""])[0]
            db.adicionar_tarefa(titulo, descricao)

        elif path == "/alternar":
            task_id = int(query["id"][0])
            db.alternar_tarefa(task_id)

        elif path == "/atualizar":
            task_id = int(query["id"][0])
            titulo = data.get("titulo", [""])[0]
            descricao = data.get("descricao", [""])[0]
            db.atualizar_tarefa(task_id, titulo, descricao)

        elif path == "/excluir":
            task_id = int(query["id"][0])
            db.excluir_tarefa(task_id)

        else:
            self.send_response(404)
            self.end_headers()
            return

        self._redirect("/")

    def mandar_pagina(self, html: str):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def _redirect(self, location: str):
        self.send_response(303)
        self.send_header("Location", location)
        self.end_headers()


if __name__ == "__main__":
    db.iniciar_banco()
    servidor = HTTPServer(("localhost", 8000), TaskHandler)
    print("Servidor rodando em http://localhost:8000")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
        servidor.server_close()
