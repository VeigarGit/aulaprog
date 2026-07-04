import sqlite3
from datetime import datetime
from typing import List, Dict, Any

DB_NAME = "dados_clientes.db"

def conectar_banco() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn

def criar_tabelas() -> None:
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL DEFAULT 'pendente',
            data_criacao TEXT NOT NULL,
            deadline TEXT,
            categoria_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    """)

    conn.commit()
    conn.close()
def inserir_tarefas(titulo, descricao, data_criacao, deadline, categoria_id=None):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tarefas(titulo, descricao, data_criacao, deadline, categoria_id) VALUES(?, ?, ?, ?, ?)""",
         (titulo, descricao, data_criacao, deadline, categoria_id))
    conn.commit()
    tarefa_id = cursor.lastrowid
    conn.close()

    return tarefa_id
def listar_tarefas(status=None):
    conn = conectar_banco()
    cursor = conn.cursor()

    if status == None:
        cursor.execute("SELECT * FROM tarefas")
    else:
        cursor.execute("SELECT * FROM tarefas WHERE status = ?", (status,))
    
    linhas = cursor.fetchall()

    tarefas = [dict(linha) for linha in linhas]

    conn.close()
    return tarefas
def atualizar_status_tarefa(id, novo_status):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("UPDATE tarefas SET status = ? WHERE id = ?", (novo_status, id))

    conn.commit()
    conn.close()

def excluir_tarefa(id):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))

    conn.commit()
    conn.close()

def editar_tarefa(id, titulo, descricao):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ?",(titulo, descricao, id))

    conn.commit()
    conn.close()