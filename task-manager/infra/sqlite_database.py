import sqlite3
from infra.database_interface import GerenciadorBancos

# Classe que usa o SQLite para gerenciar o banco de dados || Alto Nível
class GerenciadorSqlite(GerenciadorBancos):
    def __init__(self,DATABASE_NAME : str):
        self._database_name = DATABASE_NAME
        super().__init__()

    def conectar_ao_banco(self):
        try:
            conexao = sqlite3.connect(self._database_name)
            print("Conexão com o banco SQLite estabelecida com sucesso.")
            return conexao
        except sqlite3.OperationalError as e:
            # Em produção, prefira 'raise' para que o sistema saiba que falhou.
            raise ConnectionError(f"Houve um erro de conexão com o banco: {e}")

    def desconectar_do_banco(self, conexao):
        try:
            if conexao:
                conexao.close()
                print("Conexão SQLite fechada com sucesso.")
        except Exception as e:
            print(f"Erro ao fechar a conexão: {e}")

if __name__ == "__main__":
    DATABASE_NAME = "MeuBanco.db"
    db = GerenciadorSqlite(DATABASE_NAME)
    conn = db.conectar_ao_banco()
    db.desconectar_do_banco(conn)