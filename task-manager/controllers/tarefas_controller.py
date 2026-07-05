from repositorios.local_repo import LocalTarefaRepository
from repositorios.sqlite_repo import SqliteTarefaRepository
from repositorios.repository import TarefaRepositoryInterface

from entidades.tarefas_use_cases import (
    CriarTarefaUC,
    BuscarTarefaUC,
    RemoverTarefaUC,
    ListarTarefasUC,
    ConcluirTarefaUC,
    PenderTarefaUC,
    ListarTarefaStatusUC
)

# Com todos os meus usecases criados posso executar cada um deles pelo principio da segregação
class TarefaController:
    def __init__(self, repository):
        self.criar_uc = CriarTarefaUC(repository)
        self.buscar_uc = BuscarTarefaUC(repository)
        self.remover_uc = RemoverTarefaUC(repository)
        self.listar_uc = ListarTarefasUC(repository)
        self.concluir_uc = ConcluirTarefaUC(repository)
        self.pender_uc = PenderTarefaUC(repository)
        self.listar_status_uc = ListarTarefaStatusUC(repository)

    def criar_tarefa(self, nome):
        self.criar_uc.execute(nome)

    def buscar_tarefa(self, tarefa_id):
        return self.buscar_uc.execute(tarefa_id)

    def remover_tarefa(self, tarefa_id):
        self.remover_uc.execute(tarefa_id)

    def listar_tarefas(self):
        return self.listar_uc.execute()

    def concluir_tarefa(self, tarefa_id):
        self.concluir_uc.execute(tarefa_id)

    def pender_tarefa(self, tarefa_id):
        self.pender_uc.execute(tarefa_id)

    def listar_por_status(self, status):
        return self.listar_status_uc.execute(status)
    