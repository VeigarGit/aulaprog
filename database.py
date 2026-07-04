import sqlite3
from datetime import date, datetime
from typing import List, Dict, Any

DB_NAME = "notas_fiscais.db"

def conectar_banco() -> sqlite3.Connection: 
    #Conecta ao banco
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  
    return conn

def CriaTabelas() -> None:
    #Cria as tarefas caso elas n existam
    conn = conectar_banco()
    cursor = conn.cursor()

    #Cria a tabela para as tarefas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarefa TEXT NOT NULL,
            descricao TEXT,
            data_criacao TEXT,
            data_limite TEXT,
            data_conclusao TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()
    print("Tabelas criadas com sucesso!")

def GeraTarefa(tarefa: str, descricao: str, data_criacao: date, data_limite: date, data_conclusao: date, status: str) -> int:
    #Gera as tarefas
    conn = conectar_banco()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO tarefas (tarefa, descricao, data_criacao, data_limite, data_conclusao, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (tarefa, descricao, date.today(), data_limite, None, status))
        conn.commit()
        tarefa_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        # Tarefa já existe → busca o ID
        cursor.execute("SELECT id FROM tarefas WHERE tarefa = ?", (tarefa,))
        tarefa_id = cursor.fetchone()[0]

    conn.close()
    return tarefa_id

def ListarTarefas() -> List[Dict[str, Any]]:
    #Faz a lista das tarefas
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def MudarStatus(tarefa_id: str, status: str) -> None:
    #Muda o status para concluido, em andamento ou pendente 
    #pendete = quando passa da data limite e não foi concluida
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tarefas SET status = ?
        WHERE id = ? 
    """, (status, tarefa_id))
    conn.commit()
    conn.close()

def AtualizarTarefa(tarefa_id: str, tarefa: str, descricao: str, data_limite: str, status: str) -> None:
    #Atualiza as tarefas
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tarefas
        SET tarefa = ?, descricao = ?, data_limite = ?, status = ?
        WHERE id = ?
    """, (tarefa, descricao, data_limite, status, tarefa_id))
    conn.commit()
    conn.close()

def BuscarPorStatus(status: str) -> List[Dict[str, Any]]:
    #Busca as tarefas por status
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas WHERE status = ?", (status,))
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas

def DeleteTarefa(tarefa_id: str) -> None:
    #Exclui
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM tarefas WHERE id = ?
    """, (tarefa_id,))
    conn.commit()
    conn.close()

def BuscarPorId(tarefa_id: str) -> Dict[str, Any]:
    #Busca por id
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (tarefa_id,))
    tarefa = cursor.fetchone()
    conn.close()
    return tarefa