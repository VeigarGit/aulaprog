from http.server import BaseHTTPRequestHandler
from database import list_tasks, insert_task, update_status_task, delete_task, src_task_id, edit_task
from datetime import datetime
from urllib.parse import parse_qs, urlparse

def page(conteudo):
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
            task_id = int(self.path.split("/")[-1])
            task = src_task_id(task_id)
            conteudo = f"""
            <h1>Editar Tarefas</h1>
            <h1>Editar Tarefas</h1>
            <form method="POST" action="/editar/{task['id']}">
                <label for="titulo">Título:</label>
                <input type="text" id="titulo" name="titulo" value="{task['title']}" class="form-control mb-2">
                
                <label for="descricao">Descrição:</label>
                <input type="text" id="descricao" name="descricao" value="{task['description']}" class="form-control mb-2">
                
                <button type="submit" class="btn btn-primary">Salvar</button>
            </form>
            """
        else:
            query = urlparse(self.path).query
            params = parse_qs(query)
            status = params.get("status", [None])[0]
            tasks = list_tasks(status)
            linhas_html = ""
            for task in tasks:
                # Updated to use 'title' and 'status'
                linhas_html += f"""
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <span>{task['title']} - {task['status']}</span>
                    <span>
                        <a href="/editar/{task['id']}" class="btn btn-secondary btn-sm">Editar</a>
                        <form method="POST" action="/concluir/{task['id']}" style="display:inline">
                            <button type="submit" class="btn btn-success btn-sm">Concluir</button>
                        </form>
                        <form method="POST" action="/excluir/{task['id']}" style="display:inline">
                            <button type="submit" class="btn btn-danger btn-sm">Excluir</button>
                        </form>
                    </span>
                </li>
                """
            
            # Updated status links to match English database defaults ('to do' and 'completed')
            conteudo = f"""<h1>Minhas Tarefas</h1>
            <p>
                <a href="/" class="btn btn-outline-primary btn-sm">Todas</a>
                <a href="/?status=to do" class="btn btn-outline-primary btn-sm">Pendentes</a>
                <a href="/?status=completed" class="btn btn-outline-primary btn-sm">Concluídas</a>
            </p>
            <ul class="list-group mb-4">{linhas_html}</ul>

            <form method="POST" action="/adicionar">
                <input type="text" name="titulo" placeholder="Título" class="form-control mb-2">
                <input type="text" name="descricao" placeholder="Descrição" class="form-control mb-2">
                <button type="submit" class="btn btn-primary">Adicionar</button>
            </form>
            """

        html = page(conteudo)

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
            descricao = dados.get("descricao",[""])[0]
            
            # Added a default deadline (today) so the database stops crashing!
            default_deadline = datetime.now().strftime("%Y-%m-%d")
            insert_task(titulo, descricao, datetime.now().isoformat(), default_deadline, None)
            
        elif self.path.startswith("/concluir"):
            tarefa_id = int(self.path.split("/")[-1])
            # Updated status string to match English
            update_status_task(tarefa_id, "completed")
            
        elif self.path.startswith("/excluir"):
            tarefa_id = int(self.path.split("/")[-1])
            delete_task(tarefa_id)
            
        elif self.path.startswith("/editar/"):
            tarefa_id = int(self.path.split("/")[-1])
            tamanho = int(self.headers["Content-Length"])
            corpo = self.rfile.read(tamanho).decode("utf-8")
            dados = parse_qs(corpo)
            titulo = dados["titulo"][0]
            descricao = dados.get("descricao",[""])[0]
            edit_task(tarefa_id, titulo, descricao)
            
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()