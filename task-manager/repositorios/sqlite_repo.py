from infra.sqlite_database import GerenciadorSqlite
from entidades.tarefa import Tarefa,StatusTarefa
from repositorios.repository import TarefaRepositoryInterface

class SqliteTarefaRepository(TarefaRepositoryInterface):
    def __init__(self,nome_banco):
        self.database = GerenciadorSqlite(str(nome_banco)+".db")
        self.criar_tabelas()
        super().__init__()

    def criar_tabelas(self):
        conn = self.database.conectar_ao_banco()
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS tarefas ( tarefa_id TEXT PRIMARY KEY, nome TEXT NOT NULL , status TEXT NOT NULL , data_criacao  DATE NOT NULL, data_alteracao DATE NOT NULL)")
        conn.commit()
        self.database.desconectar_do_banco(conn)

    def salvar(self, tarefa):
        conn = self.database.conectar_ao_banco()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (tarefa_id,nome,status,data_criacao,data_alteracao) VALUES (?, ?, ?, ?, ?)", (str(tarefa.tarefa_id),tarefa.nome,tarefa.status.name, tarefa.data_criacao.isoformat(),tarefa.data_ultima_alteracao.isoformat()),)
        conn.commit()
        self.database.desconectar_do_banco(conn)

    def buscar_por_id(self, tarefa_id):
        print(f"==== Buscando id {tarefa_id} ====")
        conn = self.database.conectar_ao_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas WHERE tarefa_id = ?",(str(tarefa_id),))
        resultado = cursor.fetchone()
        self.database.desconectar_do_banco(conn)

        if resultado:
            #Originalemente o retorno é uma tupla, preciso alterar para um Objeto para que a Entidade entenda que é um objeto Tarefa e possa modificar seus status
            return Tarefa.recuperar(
                tarefa_id=resultado[0],
                nome=resultado[1],
                status=StatusTarefa[resultado[2]],
                data_criacao=resultado[3],
                data_ultima_alteracao=resultado[4]
            )
        else:
            return None
    
    def listar(self):
        conn = self.database.conectar_ao_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas")
        rows = cursor.fetchall()
        self.database.desconectar_do_banco(conn)
        lista_tarefas = []
        for tag in rows:
            lista_tarefas.append(
                Tarefa.recuperar(
                    tarefa_id=tag[0],
                    nome=tag[1],
                    status=StatusTarefa[tag[2]],
                    data_criacao=tag[3],
                    data_ultima_alteracao=tag[4]
            ))
        return lista_tarefas
    
    def listar_por_status(self,status_value):
        conn = self.database.conectar_ao_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas WHERE status = ?",(status_value,))
        rows = cursor.fetchall()
        self.database.desconectar_do_banco(conn)
        # Se finalizar acima tenho o retorno de Tuplas Imutaveis, mas eventualmente posso querer mudar elas
        # Faz sentida ter uma lista de objetos (Tarefa)
        lista_tarefas = []
        for tag in rows:
            lista_tarefas.append(
                Tarefa.recuperar(
                    tarefa_id=tag[0],
                    nome=tag[1],
                    status=StatusTarefa[tag[2]],
                    data_criacao=tag[3],
                    data_ultima_alteracao=tag[4]
            ))
        return lista_tarefas
    
    def atualizar_tarefa(self,tarefa_id,status_value):
        conn = self.database.conectar_ao_banco()
        cursor = conn.cursor()
        cursor.execute("UPDATE tarefas set status = ? WHERE tarefa_id = ?",(status_value,str(tarefa_id),))
        conn.commit()
        self.database.desconectar_do_banco(conn)

    def remover(self, tarefa_id):
        conn = self.database.conectar_ao_banco()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE tarefa_id = ?",(str(tarefa_id),))
        conn.commit()
        print(F"Deleção do item {tarefa_id} em {cursor.rowcount}")
        self.database.desconectar_do_banco(conn)