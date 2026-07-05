from uuid import uuid4
from enum import Enum
import datetime

class StatusTarefa(Enum):
    PENDENTE = "Pendente"
    CONCLUIDA = "Concluida"

# Vira uma entidade, pois cada tarefa por mais que repetida é única
class Tarefa:
    def __init__(self,nome):
        self.tarefa_id = uuid4()
        self.nome = nome
        self.status = StatusTarefa.PENDENTE
        self.data_criacao = datetime.date.today()
        self.data_ultima_alteracao = datetime.date.today()

    @classmethod
    def recuperar(cls, tarefa_id, nome, status, data_criacao, data_ultima_alteracao):
        tarefa = cls(nome)
        tarefa.tarefa_id = tarefa_id
        tarefa.status = status
        tarefa.data_criacao = data_criacao
        tarefa.data_ultima_alteracao = data_ultima_alteracao
        return tarefa

    def concluir(self):
        self.status = StatusTarefa.CONCLUIDA
        #self.data_ultima_alteracao = datetime.date.today()
        return self.status 
    

    def pender(self):
        self.status = StatusTarefa.PENDENTE
        #self.data_ultima_alteracao = datetime.date.today()
        return self.status


    def __str__(self):
        return (f"Tarefa : Id {self.tarefa_id} Nome {self.nome} Status : {self.status} Data_Criação : {self.data_criacao}  Data_Atualizacao: {self.data_ultima_alteracao}")
    
