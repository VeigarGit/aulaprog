import sqlite3
from datetime import datetime
from typing import List, Dict, Any

DB_NAME = "task_manager.db"


def database_conectar() -> sqlite3.Connection:
    """Conecta ao banco de dados SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
    return conn


def criar_tabelas() -> None:
    """Cria as tabelas necessárias se não existirem."""
    conn = database_conectar()
    cursor = conn.cursor()

    # Tabela de Fornecedores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL,
            data_criacao TEXT NOT NULL
        )
    """)

    # # Tabela de Notas Fiscais
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS categorias (
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         numero_nf TEXT UNIQUE,
    #         data_emissao TEXT,
    #         tarefa_id INTEGER,
    #         valor_total REAL,
    #         FOREIGN KEY (tarefa_id) REFERENCES fornecedores(id)
    #     )
    # """)

    conn.commit()
    conn.close()
    print("Tabelas criadas com sucesso!")


def inserir_tarefa(titulo: str, descricao: str = "") -> int:
    conn = database_conectar()
    cursor = conn.cursor()
    cursor.execute("""
            INSERT INTO tarefas (titulo, descricao, status, data_criacao)
            VALUES (?, ?, 'pendente', ?)
        """, (titulo, descricao, datetime.now().isoformat()))
    conn.commit()
    tarefa_id = cursor.lastrowid
    conn.close()
    return tarefa_id

def listar_tarefas(filtro: str = None) -> List[Dict[str, Any]]:
    conn = database_conectar()
    cursor = conn.cursor()
    if filtro in ("pendente", "concluida"):
        cursor.execute("SELECT * FROM tarefas WHERE status = ? ORDER BY data_criacao DESC", (filtro,))
    else:
        cursor.execute("SELECT * FROM tarefas ORDER BY data_criacao DESC")
    tarefas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return tarefas

def database_atualizar_status(tarefa_id: int, status: str) -> None:
    conn = database_conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tarefas SET status = ? WHERE id = ?", (status, tarefa_id)
    )
    conn.commit()
    conn.close()

def atualizar_tarefa(tarefa_id: int, titulo: str = None, descricao:
    str = None) -> None:
    conn = database_conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ?", (titulo, descricao, tarefa_id)
    )
    conn.commit()
    conn.close()

def excluir_tarefa(tarefa_id: int) -> None:
    conn = database_conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    conn.commit()
    conn.close()

