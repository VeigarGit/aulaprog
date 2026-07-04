from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader
import database

env = Environment(loader=FileSystemLoader("site"))

class MeuHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path == "/":
            self._listar_tarefas(params)

        elif path == "/editar":
            self._form_editar(params)

        elif path.startswith("/static/"):
            self._servir_estatico(path)

        elif path == "/concluir":
            self._concluir_tarefa(params)

        elif path == "/excluir":
            self._excluir_tarefa(params)

        else:
            self._erro404()

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length).decode("utf-8")
        dados = parse_qs(body)

        if self.path == "/adicionar":
            titulo = dados.get("titulo", [""])[0]
            descricao = dados.get("descricao", [""])[0]
            database.inserir_tarefa(titulo, descricao)
            self._redirecionar("/")

        elif self.path == "/atualizar":
            tarefa_id = int(dados.get("id", [0])[0])
            titulo = dados.get("titulo", [""])[0]
            descricao = dados.get("descricao", [""])[0]
            database.atualizar_tarefa(tarefa_id, titulo, descricao)
            self._redirecionar("/")
        else:
            self._erro404()
    
    def _listar_tarefas(self, params):
        filtro = params.get("filtro", [None])[0]
        tarefas = database.listar_tarefas(filtro)

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        template = env.get_template("index.html")
        html = template.render(tarefas=tarefas)
        self.wfile.write(html.encode("utf-8"))

    def _form_editar(self, params):
        tarefa_id = int(params.get("id", [0])[0])
        conn = database.database_conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
        tarefa = dict(cursor.fetchone())
        conn.close()

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        template = env.get_template("editar.html")
        html = template.render(tarefa=tarefa)
        self.wfile.write(html.encode("utf-8"))

    def _concluir_tarefa(self, params):
        tarefa_id = int(params.get("id", [0])[0])
        status = params.get("status", ["pendente"])[0]
        database.database_atualizar_status(tarefa_id, status)
        if status == "concluida":
            self._redirecionar("/?filtro=concluida")
        else:
            self._redirecionar("/?filtro=pendente")    

    def _excluir_tarefa(self, params):
        tarefa_id = int(params.get("id", [0])[0])
        database.excluir_tarefa(tarefa_id)
        self._redirecionar("/")    

    def _servir_estatico(self, path):
        caminho = path.lstrip("/")
        try:
            with open(caminho, "rb") as f:
                conteudo = f.read()
            if path.endswith(".css"):
                self.send_header("Content-type", "text/css; charset=utf-8")
            elif path.endswith(".js"):
                self.send_header("Content-type", "application/javascript")
            else:
                self.send_header("Content-type", "application/octet-stream")
            self.send_response(200)
            self.end_headers()
            self.wfile.write(conteudo)
        except FileNotFoundError:
            self._erro404()
    
    def _redirecionar(self, destino):
        self.send_response(302)
        self.send_header("Location", destino)
        self.end_headers()

    def _erro404(self):
        self.send_response(404)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Página não encontrada".encode("utf-8"))