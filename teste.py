from database import criar_tabelas, inserir_tarefas
from datetime import datetime

criar_tabelas()

inserir_tarefas(
    titulo = "Programar tudo",
    descricao = "Programação completa da tarefa pedida pelo laboratorio",
    data_criacao=datetime.now().isoformat(),
    deadline = None,
    categoria_id = None
)
print("Tarefa inserida")