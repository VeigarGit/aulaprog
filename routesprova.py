import urllib.parse
from http.server import BaseHTTPRequestHandler
from provadatabase import inserir_tarefa, atualizar_status, excluir_tarefas, listar_todas_tarefas, filtrar_tarefas_por_status, editar_tarefa

class GerenciadorHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        url_parseada = urllib.parse.urlparse(self.path)
        
        if url_parseada.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            parametros = urllib.parse.parse_qs(url_parseada.query)
            status_filtro = parametros.get('status', [None])[0]
            
            if status_filtro:
                tarefas = filtrar_tarefas_por_status(status_filtro)
            else:
                tarefas = listar_todas_tarefas()
                
            html_tarefas = ""
            if tarefas:
                for t in tarefas:
                    cor_badge = "bg-warning text-dark" if t[3] == "Pendente" else "bg-success"
                    
                    # Cria o botão de concluir apenas se a tarefa estiver Pendente
                    btn_concluir = f'<a href="/concluir_form?id={t[0]}" class="btn btn-outline-success btn-sm" title="Marcar como Concluída">✓</a>' if t[3] == "Pendente" else ""
                    
                    html_tarefas += f"""
                    <li class="list-group-item d-flex justify-content-between align-items-center mb-2 border rounded shadow-sm">
                        <div class="ms-2 me-auto">
                            <div class="fw-bold">ID: {t[0]} - {t[1]}</div>
                            <span class="text-muted small">{t[2]}</span><br>
                            <small class="text-secondary">Criada em: {t[4]}</small>
                        </div>
                        <div class="d-flex flex-column align-items-end gap-2">
                            <span class="badge {cor_badge} rounded-pill">{t[3]}</span>
                            <div class="btn-group">
                                {btn_concluir}
                                <a href="/excluir_form?id={t[0]}" class="btn btn-outline-danger btn-sm" title="Excluir Tarefa">🗑️</a>
                            </div>
                        </div>
                    </li>
                    """
            else:
                html_tarefas = "<div class='alert alert-info'>Nenhuma tarefa encontrada com este filtro.</div>"
            
            html = f"""
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Minhas Tarefas</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>
            <body class="bg-light pb-5">
                
                <div class="container mt-4" style="max-width: 900px;">
                    <h1 class="text-center mb-4 text-primary fw-bold">Gerenciador de Tarefas</h1>
                    
                    <div class="row g-4">
                        <div class="col-md-4">
                            
                            <div class="card shadow-sm mb-4">
                                <div class="card-header bg-primary text-white fw-bold">Nova Tarefa</div>
                                <div class="card-body">
                                    <form action="/adicionar" method="POST">
                                        <div class="mb-2">
                                            <input type="text" class="form-control" name="titulo" placeholder="Título da Tarefa" required>
                                        </div>
                                        <div class="mb-3">
                                            <textarea class="form-control" name="descricao" rows="2" placeholder="Descrição" required></textarea>
                                        </div>
                                        <button type="submit" class="btn btn-primary w-100">Cadastrar</button>
                                    </form>
                                </div>
                            </div>

                            <div class="card shadow-sm mb-4 border-info">
                                <div class="card-header bg-info text-dark fw-bold">Editar Tarefa</div>
                                <div class="card-body">
                                    <form action="/editar" method="POST">
                                        <div class="mb-2">
                                            <input type="number" class="form-control" name="id" placeholder="ID da Tarefa" min="1" required>
                                        </div>
                                        <div class="mb-2">
                                            <input type="text" class="form-control" name="titulo" placeholder="Novo Título" required>
                                        </div>
                                        <div class="mb-3">
                                            <input type="text" class="form-control" name="descricao" placeholder="Nova Descrição" required>
                                        </div>
                                        <button type="submit" class="btn btn-info w-100 text-white">Salvar Edição</button>
                                    </form>
                                </div>
                            </div>

                        </div>

                        <div class="col-md-8">
                            <div class="card shadow-sm h-100">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center">
                                    <span class="fw-bold">Sua Lista</span>
                                    <div class="btn-group btn-group-sm">
                                        <a href="/" class="btn btn-outline-light">Todas</a>
                                        <a href="/?status=Pendente" class="btn btn-outline-light">Pendentes</a>
                                        <a href="/?status=Concluída" class="btn btn-outline-light">Concluídas</a>
                                    </div>
                                </div>
                                <div class="card-body">
                                    <ul class="list-group list-group-flush">
                                        {html_tarefas}
                                    </ul>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
            
        elif self.path.startswith('/concluir_form'):
            query = urllib.parse.urlparse(self.path).query
            parametros = urllib.parse.parse_qs(query)
            id_tarefa = parametros.get('id', [''])[0]
            
            if id_tarefa:
                atualizar_status(id_tarefa, "Concluída")
                
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

        elif self.path.startswith('/excluir_form'):
            query = urllib.parse.urlparse(self.path).query
            parametros = urllib.parse.parse_qs(query)
            id_tarefa = parametros.get('id', [''])[0]
            
            if id_tarefa:
                excluir_tarefas(id_tarefa)
                
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

    def do_POST(self):
        if self.path == '/adicionar':
            tamanho_conteudo = int(self.headers.get('Content-Length', 0))
            corpo_requisicao = self.rfile.read(tamanho_conteudo).decode('utf-8')
            
            dados = urllib.parse.parse_qs(corpo_requisicao)
            titulo = dados.get('titulo', [''])[0].strip()
            descricao = dados.get('descricao', [''])[0].strip()
            
            if titulo and descricao:
                inserir_tarefa(titulo, descricao, "Pendente")
            
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
            
        elif self.path == '/editar':
            tamanho_conteudo = int(self.headers.get('Content-Length', 0))
            corpo_requisicao = self.rfile.read(tamanho_conteudo).decode('utf-8')
            
            dados = urllib.parse.parse_qs(corpo_requisicao)
            id_tarefa = dados.get('id', [''])[0]
            titulo = dados.get('titulo', [''])[0].strip()
            descricao = dados.get('descricao', [''])[0].strip()
            
            if id_tarefa and titulo and descricao:
                editar_tarefa(id_tarefa, titulo, descricao)
                
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()