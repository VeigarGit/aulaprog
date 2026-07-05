import sqlite3
from abc import ABC,abstractmethod

# Classe abstrata : Gerenciador de banco de dados || Interface 
class GerenciadorBancos(ABC):
    @abstractmethod
    def conectar_ao_banco(self):
        pass

    def desconectar_do_banco(self):
        pass
