import sqlite3
from datetime import datetime
from typing import List, Dict, Any

DB_NAME = "notas_fiscais.db"


def conectar_banco() -> sqlite3.Connection:
    """Conecta ao banco de dados SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
    return conn


def criar_tabelas() -> None:
    """Cria as tabelas necessárias se não existirem."""
    conn = conectar_banco()
    cursor = conn.cursor()

    # Tabela de Fornecedores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fornecedores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cnpj TEXT UNIQUE,
            endereco TEXT
        )
    """)

    # Tabela de Notas Fiscais
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notas_fiscais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_nf TEXT UNIQUE,
            data_emissao TEXT,
            fornecedor_id INTEGER,
            valor_total REAL,
            FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
        )
    """)

    # Tabela de Itens da Nota Fiscal
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens_nota (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nota_id INTEGER,
            descricao TEXT,
            quantidade INTEGER,
            valor_unitario REAL,
            valor_total REAL,
            FOREIGN KEY (nota_id) REFERENCES notas_fiscais(id)
        )
    """)

    conn.commit()
    conn.close()
    print("Tabelas criadas com sucesso!")


def inserir_fornecedor(nome: str, cnpj: str, endereco: str) -> int:
    """
    Insere um fornecedor se não existir.
    Retorna o ID do fornecedor (novo ou existente).
    """
    conn = conectar_banco()
    cursor = conn.cursor()

    # Tenta inserir. Se o CNPJ já existir, busca o ID existente.
    try:
        cursor.execute("""
            INSERT INTO fornecedores (nome, cnpj, endereco)
            VALUES (?, ?, ?)
        """, (nome, cnpj, endereco))
        conn.commit()
        fornecedor_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        # CNPJ já existe → busca o ID
        cursor.execute("SELECT id FROM fornecedores WHERE cnpj = ?", (cnpj,))
        fornecedor_id = cursor.fetchone()[0]

    conn.close()
    return fornecedor_id


def gerar_nota_fiscal(fornecedor_id: int, itens: List[Dict[str, Any]]) -> int:
    """
    Gera uma Nota Fiscal de Compra completa.
    Recebe uma lista de itens e calcula os totais.
    """
    conn = conectar_banco()
    cursor = conn.cursor()

    # Gerar número da NF (simples)
    numero_nf = f"NF-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    # Calcular valor total
    valor_total = sum(item['quantidade'] * item['valor_unitario'] for item in itens)

    # Inserir Nota Fiscal
    cursor.execute("""
        INSERT INTO notas_fiscais (numero_nf, data_emissao, fornecedor_id, valor_total)
        VALUES (?, ?, ?, ?)
    """, (numero_nf, datetime.now().isoformat(), fornecedor_id, valor_total))

    nota_id = cursor.lastrowid

    # Inserir itens
    for item in itens:
        valor_item = item['quantidade'] * item['valor_unitario']
        cursor.execute("""
            INSERT INTO itens_nota (nota_id, descricao, quantidade, valor_unitario, valor_total)
            VALUES (?, ?, ?, ?, ?)
        """, (nota_id, item['descricao'], item['quantidade'], item['valor_unitario'], valor_item))

    conn.commit()
    conn.close()

    print(f"Nota Fiscal {numero_nf} gerada com sucesso! (ID: {nota_id})")
    return nota_id


def buscar_nota_fiscal(nota_id: int) -> Dict[str, Any]:
    """Busca todos os dados de uma nota fiscal para renderização."""
    conn = conectar_banco()
    cursor = conn.cursor()

    # Buscar dados da nota + fornecedor
    cursor.execute("""
        SELECT 
            nf.id,
            nf.numero_nf,
            nf.data_emissao,
            nf.valor_total,
            f.nome as fornecedor_nome,
            f.cnpj,
            f.endereco
        FROM notas_fiscais nf
        JOIN fornecedores f ON nf.fornecedor_id = f.id
        WHERE nf.id = ?
    """, (nota_id,))

    nota = cursor.fetchone()

    if not nota:
        conn.close()
        return {}

    # Buscar itens
    cursor.execute("""
        SELECT descricao, quantidade, valor_unitario, valor_total
        FROM itens_nota
        WHERE nota_id = ?
    """, (nota_id,))

    itens = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return {
        "id": nota["id"],
        "numero_nf": nota["numero_nf"],
        "data_emissao": nota["data_emissao"],
        "valor_total": nota["valor_total"],
        "fornecedor_nome": nota["fornecedor_nome"],
        "cnpj": nota["cnpj"],
        "endereco": nota["endereco"],
        "itens": itens
    }