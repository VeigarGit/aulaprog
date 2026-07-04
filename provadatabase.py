'''primeira parte do sistema vai ser um codigo ra criar o banco de dados,
inserir tarefas, editar, excluir e etc, entao vai ser um codigo secundario
que vai ser chamado pelo main, aqui vai ter varias funções pra editar o banco de dados'''

import sqlite3 #importa a biclioteca do database
def criar_database():
    banco_de_dados= sqlite3.connect("Database_tarefas.db") #aloca a conexão na variavel banco de dados
    cursor= banco_de_dados.cursor() #utiliza a mesma variavel pra criar um cursor pra poder meixer na tabela
    cursor.execute( #execucao do cursor definindo os parametrod do db
        '''CREATE TABLE IF NOT EXISTS tarefas
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
            ''')
    banco_de_dados.commit() #confirma as mudancas
    banco_de_dados.close() # encerra a conexao
    print(f'DATABASE CRIADO COM SUCESSO')
    #seguir o padrao parecido com essa funcao pra criar as outras

def inserir_tarefa( titulo, descricao, status):
    conexao = sqlite3.connect("Database_tarefas.db")
    cursor = conexao.cursor()
    cursor.execute(
        '''INSERT INTO tarefas (titulo, descricao, status)
        VALUES (?, ?, ?)''', (titulo, descricao, status)
    )
    conexao.commit()
    conexao.close()
    print(f'A tarefa {titulo} foi criada com sucesso!')

def atualizar_status(id, statusnovo):
    conexao = sqlite3.connect("Database_tarefas.db")
    cursor = conexao.cursor()
    cursor.execute(
        '''UPDATE tarefas SET status=? WHERE id=?''', (statusnovo, id)
    )
    conexao.commit()
    conexao.close()
    print(f'Status atualizado com sucesso!')

def editar_tarefas(titulo, descricaonova):
    conexao = sqlite3.connect('Database_tarefas.db')
    cursor = conexao.cursor()
    cursor.execute(
        '''UPDATE tarefas set descricao=? WHERE titulo=?''', (descricaonova,titulo)
    )
    conexao.commit()
    conexao.close()
    print(f'A descrição da tarefa {titulo} foi atualizada com sucesso!')

def excluir_tarefas(id):
    conexao = sqlite3.connect("Database_tarefas.db")
    cursor = conexao.cursor()
    cursor.execute(
    '''DELETE from tarefas Where id=?''', (id,)
    )
    conexao.commit()
    conexao.close()
    print(f'A tarefa {id} foi removida da lista!')

def listar_todas_tarefas():
    conexao = sqlite3.connect("Database_tarefas.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    
    conexao.close()
    return tarefas

def filtrar_tarefas_por_status(status):
    conexao = sqlite3.connect("Database_tarefas.db")
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM tarefas WHERE status=?", (status,))
    tarefas = cursor.fetchall()
    
    conexao.close()
    return tarefas

def editar_tarefa(id, titulo, descricao):
    conexao = sqlite3.connect("Database_tarefas.db")
    cursor = conexao.cursor()
    
    cursor.execute("UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ?", (titulo, descricao, id))
    conexao.commit()
    
    conexao.close()