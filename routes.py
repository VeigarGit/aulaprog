from http.server import BaseHTTPRequestHandler
from database import listar_tarefas, inserir_tarefas, atualizar_status_tarefa, excluir_tarefa, buscar_tarefa_por_id, editar_tarefa
from datetime import datetime
from urllib.parse import parse_qs
class GerenciadorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/editar"):
            tarefa_id = int(self.path.split("/")[-1])
            tarefa = buscar_tarefa_por_id(tarefa_id)
            html = f"""
            <h1>Editar Tarefa</h1>
            <form method="POST" action="/editar/{tarefa['id']}">
                <input type="text" name="titulo" value="{tarefa['titulo']}">
                <input type="text" name="descricao" value="{tarefa['descricao']}">
                <button type="submit">Salvar</button>
            </form>
            """
        else:
            tarefas = listar_tarefas()
            linhas_html = ""
            for tarefa in tarefas:
                linhas_html += f"""
                <li>
                    {tarefa['titulo']} - {tarefa['status']}
                    <a href="/editar/{tarefa['id']}">Editar</a>
                    <form method="POST" action="/concluir/{tarefa['id']}" style="display:inline">
                        <button type="submit">Concluir</button>
                    </form>
                    <form method="POST" action="/excluir/{tarefa['id']}" style="display:inline">
                        <button type="submit">Excluir</button>
                    </form>
                </li>
                """
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


        