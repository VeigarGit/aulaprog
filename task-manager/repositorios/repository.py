from abc import abstractmethod,ABC

class TarefaRepositoryInterface(ABC):

    @abstractmethod
    def salvar(self, tarefa):
        pass

    @abstractmethod
    def remover(self, tarefa_id):
        pass

    @abstractmethod
    def buscar_por_id(self, tarefa_id):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def listar_por_status(self,status_value):
        pass

    @abstractmethod
    def atualizar_tarefa(self,tarefa_id,status_value):
        pass
