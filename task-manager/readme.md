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
C:.
│   main.py
│   readme.md
│   __init__.py
│
├───controllers
│   │   tarefas_controller.py
│   │   __init__.py
│   │
│   └───__pycache__
│           tarefas_controller.cpython-314.pyc
│           __init__.cpython-314.pyc
│
├───entidades
│   │   tarefa.py
│   │   tarefas_use_cases.py
│   │   __init__.py
│   │
│   └───__pycache__
│           tarefa.cpython-314.pyc
│           tarefas_use_cases.cpython-314.pyc
│           __init__.cpython-314.pyc
│
├───infra
│   │   database_interface.py
│   │   sqlite_database.py
│   │   __init__.py
│   │
│   └───__pycache__
│           database_interface.cpython-314.pyc
│           sqlite_database.cpython-314.pyc
│           __init__.cpython-314.pyc
│
└───repositorios
    │   local_repo.py
    │   repository.py
    │   sqlite_repo.py
    │   __init__.py
    │
    └───__pycache__
            local_repo.cpython-314.pyc
            repository.cpython-314.pyc
            sqlite_repo.cpython-314.pyc
            __init__.cpython-314.pyc

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

1. Clone o projeto:
```bash
git clone https://github.com/VeigarGit/aulaprog.git

2. Acesse a pasta do projeto:
cd task-manager

3. Dentro do Diretório do Projeto:
python main.py
