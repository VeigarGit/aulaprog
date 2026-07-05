from repositorios.repository import TarefaRepositoryInterface

class LocalTarefaRepository(TarefaRepositoryInterface):

    def __init__(self):
        self._tarefas = []

    def salvar(self, tarefa):
        self._tarefas.append(tarefa)

    #def remover(self, nome_tarefa):
    #    #O correto é remover por ID, mas testei a remoção por nome, já que cada UUID gera uma sequencia aleatória
    #   print(f" Tarefa a ser removida {nome_tarefa}")
    #   for t in self._tarefas:
    #       if t.nome == nome_tarefa:
    #          self._tarefas.remove(t)
    #          print("Remoção efetuada com sucesso")

    def buscar_por_id(self, tarefa_id):
        for t in self._tarefas:
            if t.tarefa_id == tarefa_id:
                return t
        return None
    
    # Função Local : Facilitadora
    def buscar_por_nome(self,nome_tarefa):
        for t in self._tarefas:
            if t.nome == nome_tarefa:
                return t

    def listar(self):
        for t in self._tarefas:
            print(t)
        return self._tarefas
    
    def listar_por_status(self, status_value):
        pass

    def atualizar_tarefa(self,tarefa_id):
        pass

    # Não me sinto seguro de que deveria ter ação que afeta a entidade aqui
    #def concluir_status_tarefa(self, nome_tarefa):
    #    t = self.buscar_por_nome(nome_tarefa)
    #    t.concluir()
    
    #def pender_status_tarefa(self, nome_tarefa):
    #    t = self.buscar_por_nome(nome_tarefa)
     #   t.pender()
