import sqlite3
from datetime import datetime

DB_ARQUIVO = "tarefas.db"

def init_db():
    conn = sqlite3.connect(DB_ARQUIVO)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT DEFAULT 'pendente',
            data_criacao TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_tarefas(status_filter=None):
    conn = sqlite3.connect(DB_ARQUIVO)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if status_filter in ['pendente', 'concluida']:
        cursor.execute('SELECT * FROM tarefas WHERE status = ? ORDER BY data_criacao DESC', (status_filter,))
    else:
        cursor.execute('SELECT * FROM tarefas ORDER BY data_criacao DESC')
        
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def adicionar_tarefa(titulo, descricao):
    conn = sqlite3.connect(DB_ARQUIVO)
    cursor = conn.cursor()
    data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cursor.execute('INSERT INTO tarefas (titulo, descricao, status, data_criacao) VALUES (?, ?, "pendente", ?)',
                   (titulo, descricao, data_criacao))
    conn.commit()
    conn.close()

def atualizar_status(tarefa_id, status):
    conn = sqlite3.connect(DB_ARQUIVO)
    cursor = conn.cursor()
    cursor.execute('UPDATE tarefas SET status = ? WHERE id = ?', (status, tarefa_id))
    conn.commit()
    conn.close()

def deletar_tarefa(tarefa_id):
    conn = sqlite3.connect(DB_ARQUIVO)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tarefas WHERE id = ?', (tarefa_id,))
    conn.commit()
    conn.close()

def editar_tarefa(tarefa_id, titulo, descricao):
    conn = sqlite3.connect(DB_ARQUIVO)
    cursor = conn.cursor()
    cursor.execute('UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ?', 
                   (titulo, descricao, tarefa_id))
    conn.commit()
    conn.close()    