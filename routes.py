from http.server import BaseHTTPRequestHandler
from database import listar_tarefas, inserir_tarefas, atualizar_status_tarefa, excluir_tarefa, buscar_tarefa_por_id, editar_tarefa
from datetime import datetime
from urllib.parse import parse_qs, urlparse


def montar_pagina(conteudo):
    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <title>Gerenciador de Tarefas</title>
    </head>
    <body>
        <div class="container mt-4">
            {conteudo}
        </div>
    </body>
    </html>
    """


class GerenciadorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/editar"):
            tarefa_id = int(self.path.split("/")[-1])
            tarefa = buscar_tarefa_por_id(tarefa_id)
            conteudo = f"""
            <h1>Editar Tarefa</h1>
            <form method="POST" action="/editar/{tarefa['id']}">
                <input type="text" name="titulo" value="{tarefa['titulo']}" class="form-control mb-2">
                <input type="text" name="descricao" value="{tarefa['descricao']}" class="form-control mb-2">
                <button type="submit" class="btn btn-primary">Salvar</button>
            </form>
            """
        else:
            query = urlparse(self.path).query
            params = parse_qs(query)
            status = params.get("status", [None])[0]
            tarefas = listar_tarefas(status)
            linhas_html = ""
            for tarefa in tarefas:
                linhas_html += f"""
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <span>{tarefa['titulo']} - {tarefa['status']}</span>
                    <span>
                        <a href="/editar/{tarefa['id']}" class="btn btn-secondary btn-sm">Editar</a>
                        <form method="POST" action="/concluir/{tarefa['id']}" style="display:inline">
                            <button type="submit" class="btn btn-success btn-sm">Concluir</button>
                        </form>
                        <form method="POST" action="/excluir/{tarefa['id']}" style="display:inline">
                            <button type="submit" class="btn btn-danger btn-sm">Excluir</button>
                        </form>
                    </span>
                </li>
                """
            conteudo = f"""<h1>Minhas Tarefas</h1>
            <p>
                <a href="/" class="btn btn-outline-primary btn-sm">Todas</a>
                <a href="/?status=pendente" class="btn btn-outline-primary btn-sm">Pendentes</a>
                <a href="/?status=concluida" class="btn btn-outline-primary btn-sm">Concluídas</a>
            </p>
            <ul class="list-group mb-4">{linhas_html}</ul>

            <form method="POST" action="/adicionar">
                <input type="text" name="titulo" placeholder="Título" class="form-control mb-2">
                <input type="text" name="descricao" placeholder="Descrição" class="form-control mb-2">
                <button type="submit" class="btn btn-primary">Adicionar</button>
            </form>
            """

        html = montar_pagina(conteudo)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


    def do_POST(self):
        if self.path == "/adicionar":
            tamanho = int(self.headers["Content-Length"])
            corpo = self.rfile.read(tamanho).decode("utf-8")
            dados = parse_qs(corpo)
            titulo = dados["titulo"][0]
            descricao = dados["descricao"][0]
            inserir_tarefas(titulo,descricao,datetime.now(), None, None)
        elif self.path.startswith("/concluir"):
            tarefa_id = int(self.path.split("/")[-1])
            atualizar_status_tarefa(tarefa_id, "concluida")
        elif self.path.startswith("/excluir"):
            tarefa_id = int(self.path.split("/")[-1])
            excluir_tarefa(tarefa_id)
        elif self.path.startswith("/editar/"):
            tarefa_id = int(self.path.split("/")[-1])
            tamanho = int(self.headers["Content-Length"])
            corpo = self.rfile.read(tamanho).decode("utf-8")
            dados = parse_qs(corpo)
            titulo = dados["titulo"][0]
            descricao = dados["descricao"][0]
            editar_tarefa(tarefa_id, titulo, descricao)
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()
