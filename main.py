from http.server import BaseHTTPRequestHandler, HTTPServer
#from os import path
from urllib.parse import urlparse, parse_qs

from datetime import datetime
import database
import templates

PORT = 8000

class TaskHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        caminho = parsed.path
        query = parse_qs(parsed.query)

        if caminho == '/':
            status = query.get('status', [''])[0]


            tarefasdb = database.ListarTarefas()

            tarefas = []
            print("DADOS DO BANCO:", type(tarefasdb[0]) if tarefasdb else "não salvou")
            for t in tarefasdb:
                tarefas.append({
                    'id': t['id'],
                    'tarefa': t['tarefa'],
                    'descricao': t['descricao'],
                    'data_criacao': t['data_criacao'],
                    'data_limite': t['data_limite'],
                    'data_conclusao': t['data_conclusao'],
                    'status': t['status']
                })
            if status == "concluida":
                tarefas = [t for t in tarefas if t["status"] == "concluida"]
            elif status == "pendente":
                tarefas = [t for t in tarefas if t["status"] == "pendente"]
            elif status == "em andamento":
                tarefas = [t for t in tarefas if t["status"] == "em andamento"]
            else:
                tarefas = tarefas
            html = templates.render_tarefas(tarefas, status)
            #print(f"---------------------------------")
            #print(f"Requisição GET para {caminho}")
            self.send_html(html)

        elif caminho == '/editar':
            tarefa_id = query.get('id', [''])[0]
            tarefa_id = tarefa_id.replace('(', '').replace(')', '').replace(',', '').strip()
            if tarefa_id:
                tarefasdb = database.BuscarPorId(int(tarefa_id))
                
                if tarefasdb:
                    html = templates.render_edita(tarefasdb)
                    self.send_html(html)
                else:
                    self.send_error(404, 'Tarefa não encontrada')
            else:
                self.send_error(400, 'ID da tarefa não fornecido')

        elif caminho == '/status':
            tarefa_id = query.get('id', [''])[0]
            if tarefa_id:
                tarefasdb = database.BuscarPorId(int(tarefa_id))
                if tarefasdb:
                    nova_status = 'em andamento' if tarefasdb['status'] == 'pendente' else ('concluida' if tarefasdb['status'] == 'em andamento' else 'pendente')
                    database.MudarStatus(int(tarefa_id), nova_status)
                    self.send_response(303)
                    self.send_header("Location", "/")
                    self.end_headers()
                else:
                    self.send_error(404, 'Tarefa não encontrada')
            else:
                self.send_error(400, 'ID da tarefa não fornecido')



        elif caminho == '/deletar':
            tarefa_id = query.get('id', [''])[0]
            database.DeleteTarefa(int(tarefa_id))
            self.send_response(303)
            self.send_header("Location", "/")
            self.end_headers()
        else:
            self.send_error(404, 'Page not found')








    def do_POST(self):
        parsed = urlparse(self.path)
        caminho = parsed.path
        query = parse_qs(parsed.query)
        if caminho == '/tarefas':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = parse_qs(post_data)
            tarefa = data.get('tarefa', [''])[0]
            descricao = data.get('descricao', [''])[0]
            data_criacao = data.get('data_criacao', [''])[0]
            data_limite = data.get('data_limite', [''])[0]
            data_conclusao = data.get('data_conclusao', [''])[0]
            status = data.get('status', [''])[0]
            database.GeraTarefa(tarefa, descricao, data_criacao, data_limite, data_conclusao, status)
            self.redirect('/')
            #print(f"---------------------------------")
            #print(f"Salvo com sucesso: {tarefa} - {descricao}")
        
        
        elif caminho == '/editar':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = parse_qs(post_data)

            tarefa_id = data.get('id', [''])[0]
            tarefa = data.get('tarefa', [''])[0]
            descricao = data.get('descricao', [''])[0]
            data_limite = data.get('data_limite', [''])[0]
            status = data.get('status', [''])[0]
            database.AtualizarTarefa(tarefa_id, tarefa, descricao, data_limite, status)

            self.redirect('/')

    
    def send_html(self, html: str):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def redirect(self, location: str):
        self.send_response(303)
        self.send_header("Location", location)
        self.end_headers()


def startServer():
    database.CriaTabelas()

    server_address = ('', PORT)
    httpd = HTTPServer(server_address, TaskHandler)
    print(f"Servidor rodando em http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor desligado pelo usuário.")
        httpd.server_close()


if __name__ == "__main__":
    startServer()


