import sqlite3
from datetime import datetime

DB_NAME = "taskmanager.db"


def conectar_banco():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def criar_tabelas():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT DEFAULT '',
            status TEXT DEFAULT 'pendente',
            data_criacao TEXT NOT NULL,
            categoria_id INTEGER,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM categorias")
    if cursor.fetchone()[0] == 0:
        categorias_padrao = ["Trabalho", "Estudo", "Pessoal", "Outros"]
        for nome in categorias_padrao:
            cursor.execute("INSERT INTO categorias (nome) VALUES (?)", (nome,))

    conn.commit()
    conn.close()


def inserir_tarefa(titulo, descricao="", status="pendente", categoria_id=None):
    conn = conectar_banco()
    cursor = conn.cursor()
    data_criacao = datetime.now().isoformat()
    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao, status, data_criacao, categoria_id)
        VALUES (?, ?, ?, ?, ?)
    """, (titulo, descricao, status, data_criacao, categoria_id))
    conn.commit()
    tarefa_id = cursor.lastrowid
    conn.close()
    return tarefa_id


def listar_tarefas(filtro="todas"):
    conn = conectar_banco()
    cursor = conn.cursor()

    if filtro == "pendentes":
        cursor.execute("""
            SELECT t.*, c.nome as categoria_nome
            FROM tarefas t
            LEFT JOIN categorias c ON t.categoria_id = c.id
            WHERE t.status = 'pendente'
            ORDER BY t.data_criacao DESC
        """)
    elif filtro == "concluidas":
        cursor.execute("""
            SELECT t.*, c.nome as categoria_nome
            FROM tarefas t
            LEFT JOIN categorias c ON t.categoria_id = c.id
            WHERE t.status = 'concluida'
            ORDER BY t.data_criacao DESC
        """)
    else:
        cursor.execute("""
            SELECT t.*, c.nome as categoria_nome
            FROM tarefas t
            LEFT JOIN categorias c ON t.categoria_id = c.id
            ORDER BY t.data_criacao DESC
        """)

    tarefas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return tarefas


def buscar_tarefa(tarefa_id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.*, c.nome as categoria_nome
        FROM tarefas t
        LEFT JOIN categorias c ON t.categoria_id = c.id
        WHERE t.id = ?
    """, (tarefa_id,))
    tarefa = cursor.fetchone()
    conn.close()
    return dict(tarefa) if tarefa else None


def atualizar_tarefa(tarefa_id, titulo, descricao, categoria_id=None):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tarefas SET titulo = ?, descricao = ?, categoria_id = ?
        WHERE id = ?
    """, (titulo, descricao, categoria_id, tarefa_id))
    conn.commit()
    conn.close()


def atualizar_status(tarefa_id, status):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET status = ? WHERE id = ?", (status, tarefa_id))
    conn.commit()
    conn.close()


def excluir_tarefa(tarefa_id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    conn.commit()
    conn.close()


def listar_categorias():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM categorias ORDER BY nome")
    categorias = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return categorias
