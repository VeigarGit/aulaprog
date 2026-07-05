# Task Manager : Python + SQLite

Sistema de gerenciamento de tarefas desenvolvido em Python
---

## Funcionalidades Atuais

- Criar tarefas
- Remover tarefas por ID
- Concluir tarefas
- Marcar tarefas como pendentes
- Listar todas as tarefas
- Filtrar tarefas por status (pendente/concluída)

---

## Estrutura do Projeto
``` bash
C:.
│   main.py
│   readme.md
├───controllers
│   │   tarefas_controller.py
│
├───entidades
│   │   tarefa.py
│   │   tarefas_use_cases.py
│
├───infra
│   │   database_interface.py
│   │   sqlite_database.py
│
└───repositorios
    │   local_repo.py
    │   repository.py
    │   sqlite_repo.py

```
## Um pouco da Arquitetura

O projeto segue uma separação em camadas:

- **controllers** → camada responsável pela comunicação com o usuário
- **entidades** → regras de negócio (use cases e entidades)
- **repositorios** → acesso a dados (SQLite ou local)
- **infra** → infraestrutura de banco de dados e interfaces

Tecnologias

- Python 3.14
- SQLite


## Como executar
```bash
1. Clone o projeto:
git clone https://github.com/VeigarGit/aulaprog.git

2. Acesse a pasta do projeto:
cd task-manager

3. Dentro do Diretório do Projeto:
python main.py
```
