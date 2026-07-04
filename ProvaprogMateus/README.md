# Gerenciador de Tarefas (Task Manager Web)

Sistema web funcional de gerenciamento de tarefas com interface responsiva, desenvolvido em Python com `http.server`.

## Funcionalidades

- Cadastrar novas tarefas com título, descrição e categoria
- Listar todas as tarefas
- Marcar tarefas como concluídas (toggle)
- Editar e excluir tarefas
- Filtrar tarefas por status (Todas / Pendentes / Concluídas)

## Como Executar

### Pelo terminal

Entre na pasta "ProvaprogMateus" e execute o arquivo main.py

```bash
python3 main.py
```

Acesse no navegador: http://localhost:5000 para acessar o gerenciador de tarefas

## Tecnologias Utilizadas

- **http.server** (módulo nativo) — servidor HTTP base
- **SQLite3** — banco de dados relacional
- **Bootstrap 5** (CDN) — interface responsiva
- **Bootstrap Icons** (CDN) — ícones

## Estrutura do Projeto

```
main.py        — Ponto de entrada (inicia o servidor)
server.py      — Rotas e handlers HTTP (BaseHTTPRequestHandler)
database.py    — Conexão e operações com SQLite (CRUD)
templates.py   — Templates HTML com Bootstrap 5
taskmanager.db — Banco de dados SQLite (gerado automaticamente)
```
