import http.server
import database
from urllib.parse import urlparse, parse_qs
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(('Front_end')))

def redirecionar(handler, destino):
    """Função auxiliar para redirecionamento HTTP"""
    handler.send_response(303)
    handler.send_header('Location', destino)
    handler.end_headers()

def listar_tarefas(handler, parametros):
    filtro = parametros.get('filter', [None])[0]
    lista_tarefas = database.get_tarefas(filtro)
    template = env.get_template('index.html')
    html_final = template.render(tarefas=lista_tarefas)

    handler.send_response(200)
    handler.send_header('Content-type', 'text/html; charset=utf-8')
    handler.end_headers()
    handler.wfile.write(html_final.encode('utf-8'))

def concluir_tarefa(handler, parametros):
    id_tarefa = parametros.get('id', [None])[0]
    if id_tarefa:
        database.atualizar_status(id_tarefa, 'concluida')
    redirecionar(handler, '/')

def deletar_tarefa(handler, parametros):
    id_tarefa = parametros.get('id', [None])[0]
    if id_tarefa:
        database.deletar_tarefa(id_tarefa)
    redirecionar(handler, '/')

def adicionar_tarefa(handler, dados_post):
    campos = parse_qs(dados_post)
    titulo = campos.get('titulo', [''])[0].strip()
    descricao = campos.get('descricao', [''])[0].strip()

    if titulo:
        database.adicionar_tarefa(titulo, descricao)
    redirecionar(handler, '/')

def processar_edicao(handler, dados_post):
    campos = parse_qs(dados_post)
    id_tarefa = campos.get('id', [''])[0].strip()
    titulo = campos.get('titulo', [''])[0].strip()
    descricao = campos.get('descricao', [''])[0].strip()

    if id_tarefa and titulo:
        database.editar_tarefa(id_tarefa, titulo, descricao)
        
    redirecionar(handler, '/')

ROTAS_GET = {
    '/': listar_tarefas,
    '/complete': concluir_tarefa,
    '/delete': deletar_tarefa, 
}

ROTAS_POST = {
    '/add': adicionar_tarefa,
    '/edit': processar_edicao # Rota que salva os dados (POST)
}

class GerenciadorTarefas(http.server.BaseHTTPRequestHandler):
    
    def do_GET(self):
        url_analisada = urlparse(self.path)
        caminho = url_analisada.path
        parametros = parse_qs(url_analisada.query)

        # Roteamento dinâmico usando o dicionário ROTAS_GET
        if caminho in ROTAS_GET:
            funcao_controladora = ROTAS_GET[caminho]
            funcao_controladora(self, parametros)
        else:
            self.send_error(404, "Página não encontrada")

    def do_POST(self):
        url_analisada = urlparse(self.path)
        caminho = url_analisada.path
        
        # Roteamento dinâmico usando o dicionário ROTAS_POST
        if caminho in ROTAS_POST:
            tamanho_conteudo = int(self.headers['Content-Length'])
            dados_post = self.rfile.read(tamanho_conteudo).decode('utf-8')
            
            funcao_controladora = ROTAS_POST[caminho]
            funcao_controladora(self, dados_post)
        else:
            self.send_error(404, "Rota POST não encontrada")