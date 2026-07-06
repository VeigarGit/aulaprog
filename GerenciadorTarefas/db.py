import sqlite3
from typing import List, Dict, Any, Optional

DB_NAME = "tarefas.db"


def conectar() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def iniciar_banco() -> None:
    conn = conectar()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT DEFAULT '',
            concluida INTEGER DEFAULT 0,
            criada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso!")


def adicionar_tarefa(titulo: str, descricao: str = "") -> None:
    conn = conectar()
    conn.execute(
        "INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)",
        (titulo, descricao)
    )
    conn.commit()
    conn.close()


def listar_tarefas(status: Optional[str] = None) -> List[Dict[str, Any]]:
    conn = conectar()
    if status == "pending":
        rows = conn.execute(
            "SELECT * FROM tarefas WHERE concluida = 0 ORDER BY criada_em DESC"
        ).fetchall()
    elif status == "completed":
        rows = conn.execute(
            "SELECT * FROM tarefas WHERE concluida = 1 ORDER BY criada_em DESC"
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM tarefas ORDER BY criada_em DESC"
        ).fetchall()
    conn.close()
    return [dict(row) for row in rows]


def buscar_tarefa(id: int) -> Optional[Dict[str, Any]]:
    conn = conectar()
    row = conn.execute(
        "SELECT * FROM tarefas WHERE id = ?", (id,)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def alternar_tarefa(id: int) -> None:
    conn = conectar()
    conn.execute(
        "UPDATE tarefas SET concluida = NOT concluida WHERE id = ?", (id,)
    )
    conn.commit()
    conn.close()


def atualizar_tarefa(id: int, titulo: str, descricao: str) -> None:
    conn = conectar()
    conn.execute(
        "UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ?",
        (titulo, descricao, id)
    )
    conn.commit()
    conn.close()


def excluir_tarefa(id: int) -> None:
    conn = conectar()
    conn.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
