# Listo aqui as ações as quais uso a entidade
from entidades.tarefa import Tarefa
from repositorios.sqlite_repo import SqliteTarefaRepository

class CriarTarefaUC:
    def __init__(self, repository):
        #self.tarefa = Tarefa(nome_tarefa)
        #print(self.tarefa)
        # Fiz merda aqui pois toda vez que crio uma tarefa eu crio também um novo repository, isso não faz sentido
        #self.repo = TarefaRepository()
        #self.repo.salvar(self.tarefa)

        self.repository = repository

    def execute(self,nome_tarefa):
        tarefa = Tarefa(nome_tarefa)
        self.repository.salvar(tarefa)

class BuscarTarefaUC:
    def __init__(self, repository : object):
        self.repository = repository
    
    def execute(self,tarefa_id):
        return self.repository.buscar_por_id(tarefa_id)

class RemoverTarefaUC:
    def __init__(self, repository : object):
        self.repository = repository
    
    def execute(self,tarefa_id):
        #Acredito que o correto seria a tarefa de remover, buscar por id primeiro e depois remover
        self.repository.remover(tarefa_id)

class ListarTarefasUC:
    def __init__(self, repository : object):
        self.repository = repository

    def execute(self):
        return self.repository.listar()

class ConcluirTarefaUC:
    def __init__(self, repository : object):
        self.repository = repository
    
    def execute(self,tarefa_id):
        tarefa = self.repository.buscar_por_id(tarefa_id)

        if tarefa is not None:
            status = tarefa.concluir()
            self.repository.atualizar_tarefa(tarefa_id,status.name)

class PenderTarefaUC:
    def __init__(self, repository : object):
        self.repository = repository
    
    def execute(self,tarefa_id):
        tarefa = self.repository.buscar_por_id(tarefa_id)

        if tarefa is not None:
            status = tarefa.pender()
            self.repository.atualizar_tarefa(tarefa_id,status.name)

class ListarTarefaStatusUC:
    def __init__(self, repository : object):
        self.repository = repository
    
    def execute(self,status_tarefa : str):
        tarefas = self.repository.listar_por_status(status_tarefa.upper())
        return tarefas
