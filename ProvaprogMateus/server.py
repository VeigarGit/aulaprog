from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import database
from templates import (
    render_listar, render_form_adicionar, render_form_editar
)


class TaskManagerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path == "/":
            self.handle_listar(params)
        elif path == "/add":
            self.handle_form_adicionar()
        elif path.startswith("/edit/"):
            tarefa_id = int(path.split("/")[2])
            self.handle_form_editar(tarefa_id)
        else:
            self.send_404()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length).decode("utf-8")
        post_data = parse_qs(body)

        if path == "/add":
            self.handle_salvar(post_data)
        elif path.startswith("/edit/"):
            tarefa_id = int(path.split("/")[2])
            self.handle_atualizar(tarefa_id, post_data)
        elif path.startswith("/toggle/"):
            tarefa_id = int(path.split("/")[2])
            self.handle_toggle(tarefa_id)
        elif path.startswith("/delete/"):
            tarefa_id = int(path.split("/")[2])
            self.handle_excluir(tarefa_id)
        else:
            self.send_404()

    def handle_listar(self, params):
        filtro = params.get("status", ["todas"])[0]
        tarefas = database.listar_tarefas(filtro)
        categorias = database.listar_categorias()
        html = render_listar(tarefas, categorias, filtro)
        self.send_html(html)

    def handle_form_adicionar(self):
        categorias = database.listar_categorias()
        html = render_form_adicionar(categorias)
        self.send_html(html)

    def handle_form_editar(self, tarefa_id):
        tarefa = database.buscar_tarefa(tarefa_id)
        if not tarefa:
            return self.send_404()
        categorias = database.listar_categorias()
        html = render_form_editar(tarefa, categorias)
        self.send_html(html)

    def handle_salvar(self, post_data):
        titulo = post_data.get("titulo", [""])[0]
        descricao = post_data.get("descricao", [""])[0]
        categoria_raw = post_data.get("categoria_id", [None])[0]
        categoria_id = int(categoria_raw) if categoria_raw else None
        database.inserir_tarefa(titulo, descricao, categoria_id=categoria_id)
        self.redirect("/")

    def handle_atualizar(self, tarefa_id, post_data):
        titulo = post_data.get("titulo", [""])[0]
        descricao = post_data.get("descricao", [""])[0]
        categoria_raw = post_data.get("categoria_id", [None])[0]
        categoria_id = int(categoria_raw) if categoria_raw else None
        database.atualizar_tarefa(tarefa_id, titulo, descricao, categoria_id)
        self.redirect("/")

    def handle_toggle(self, tarefa_id):
        tarefa = database.buscar_tarefa(tarefa_id)
        if tarefa:
            novo_status = "concluida" if tarefa["status"] == "pendente" else "pendente"
            database.atualizar_status(tarefa_id, novo_status)
        self.redirect("/")

    def handle_excluir(self, tarefa_id):
        database.excluir_tarefa(tarefa_id)
        self.redirect("/")

    def send_html(self, html):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def redirect(self, path):
        self.send_response(302)
        self.send_header("Location", path)
        self.end_headers()

    def send_404(self):
        self.send_response(404)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>404 - Pagina nao encontrada</h1>".encode("utf-8"))
