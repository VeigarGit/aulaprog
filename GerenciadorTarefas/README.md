# Gerenciador de Tarefas

Sistema web de gerenciamento de tarefas (Task Manager) desenvolvido em Python com SQLite3, Jinja2 e Bootstrap 5.

## Tecnologias

- **Servidor:** `http.server` + `BaseHTTPRequestHandler` (stdlib)
- **Banco:** SQLite3 (stdlib)
- **Templates:** Jinja2
- **Frontend:** Bootstrap 5.3.3 via CDN (tema escuro)

## Estrutura

```
GerenciadorTarefas/
├── servidor.py        # Servidor HTTP (porta 8000)
├── db.py              # CRUD SQLite3
├── frontend/
│   ├── base.html      # Layout base + Bootstrap CDN
│   ├── index.html     # Lista de tarefas + formulário + filtros
│   └── edit.html      # Formulário de edição
├── requirements.txt   # jinja2
└── tarefas.db         # Criado automaticamente na 1ª execução
```

## Como executar

```bash
# 1. Ativar o ambiente virtual
.\venv\Scripts\activate      # Windows PowerShell

# 2. Instalar dependência
pip install jinja2

# 3. Iniciar servidor
python servidor.py

# 4. Abrir no navegador
# http://localhost:8000
```

Pressione `Ctrl + C` para parar o servidor.

## Funcionalidades

- Cadastrar nova tarefa (título + descrição)
- Listar todas as tarefas em grid responsivo
- Filtrar por status: Todas / Pendentes / Concluídas
- Marcar/desmarcar tarefa como concluída
- Editar título e descrição
- Excluir tarefa com confirmação
- Tema escuro (Bootstrap data-bs-theme="dark")

## Rotas da API

| Método | Rota | Ação |
|--------|------|------|
| GET | `/` | Lista tarefas (opcional `?status=pending` ou `?status=completed`) |
| GET | `/editar?id=N` | Formulário de edição |
| POST | `/adicionar` | Cria nova tarefa |
| POST | `/alternar?id=N` | Alterna concluído |
| POST | `/atualizar?id=N` | Salva edição |
| POST | `/excluir?id=N` | Remove tarefa |
