PAGE_HEADER = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciador de Tarefas</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        body { background-color: #f8f9fa; }
        .task-card { transition: box-shadow .2s; }
        .task-card:hover { box-shadow: 0 .25rem .75rem rgba(0,0,0,.08); }
        .task-card.concluida { opacity: .7; }
        .task-card.concluida .card-title { text-decoration: line-through; }
        .filter-btn { text-decoration: none; }
        .filter-btn.active { font-weight: 600; }
    </style>
</head>
<body>
"""

PAGE_FOOTER = """
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""


def _navbar(filtro_atual):
    return f"""
<nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
    <div class="container">
        <a class="navbar-brand" href="/">
            <i class="bi bi-check2-square"></i> Gerenciador de Tarefas
        </a>
    </div>
</nav>
<div class="container">
    <div class="d-flex gap-2 mb-3 flex-wrap">
        <a href="/" class="filter-btn btn btn-sm {'btn-primary' if filtro_atual == 'todas' else 'btn-outline-secondary'}">
            Todas
        </a>
        <a href="/?status=pendentes" class="filter-btn btn btn-sm {'btn-primary' if filtro_atual == 'pendentes' else 'btn-outline-secondary'}">
            Pendentes
        </a>
        <a href="/?status=concluidas" class="filter-btn btn btn-sm {'btn-primary' if filtro_atual == 'concluidas' else 'btn-outline-secondary'}">
            Concluídas
        </a>
        <a href="/add" class="btn btn-success btn-sm ms-auto">
            <i class="bi bi-plus-lg"></i> Nova Tarefa
        </a>
    </div>
"""


def render_listar(tarefas, categorias, filtro):
    html = PAGE_HEADER
    html += _navbar(filtro)

    if not tarefas:
        html += '<div class="alert alert-info">Nenhuma tarefa encontrada.</div>'
    else:
        html += '<div class="row g-3">'
        for t in tarefas:
            status_class = "concluida" if t["status"] == "concluida" else ""
            badge_class = "success" if t["status"] == "concluida" else "warning"
            status_label = "Concluída" if t["status"] == "concluida" else "Pendente"
            cat_badge = ""
            if t.get("categoria_nome"):
                cat_badge = f'<span class="badge bg-info text-dark">{t["categoria_nome"]}</span>'

            html += f"""
<div class="col-12 col-md-6 col-lg-4">
    <div class="card task-card {status_class} h-100">
        <div class="card-body">
            <div class="d-flex justify-content-between align-items-start mb-2">
                <h5 class="card-title mb-0">{t["titulo"]}</h5>
                {cat_badge}
            </div>
            <p class="card-text text-muted small">{t["descricao"] or "<em>Sem descrição</em>"}</p>
            <div class="d-flex justify-content-between align-items-center mt-3">
                <span class="badge bg-{badge_class}">{status_label}</span>
                <small class="text-muted">{t["data_criacao"][:10]}</small>
            </div>
            <div class="d-flex gap-2 mt-3">
                <form action="/toggle/{t["id"]}" method="post" class="d-inline">
                    <button class="btn btn-sm {'btn-success' if t['status'] == 'pendente' else 'btn-secondary'}" title="Concluído">
                        <i class="bi {'bi-check-lg' if t['status'] == 'pendente' else 'bi-arrow-counterclockwise'}"></i>
                    </button>
                </form>
                <a href="/edit/{t['id']}" class="btn btn-sm btn-outline-primary" title="Editar">
                    <i class="bi bi-pencil"></i>
                </a>
                <form action="/delete/{t["id"]}" method="post" class="d-inline" onsubmit="return confirm('Excluir esta tarefa?')">
                    <button class="btn btn-sm btn-outline-danger" title="Excluir">
                        <i class="bi bi-trash"></i>
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>"""
        html += "</div>"

    html += "</div>" + PAGE_FOOTER
    return html


def _form_tarefa(tarefa=None, categorias=None):
    titulo = tarefa["titulo"] if tarefa else ""
    descricao = tarefa["descricao"] if tarefa else ""
    categoria_id = tarefa["categoria_id"] if tarefa else ""
    acao = f"/edit/{tarefa['id']}" if tarefa else "/add"
    btn_texto = "Salvar alterações" if tarefa else "Adicionar"
    titulo_pagina = "Editar Tarefa" if tarefa else "Nova Tarefa"

    options = '<option value="">Sem categoria</option>'
    if categorias:
        for c in categorias:
            selected = " selected" if str(c["id"]) == str(categoria_id) else ""
            options += f'<option value="{c["id"]}"{selected}>{c["nome"]}</option>'

    return f"""
<div class="container">
    <div class="row justify-content-center">
        <div class="col-12 col-md-8 col-lg-6">
            <div class="card shadow-sm">
                <div class="card-body">
                    <h4 class="card-title mb-4">{titulo_pagina}</h4>
                    <form action="{acao}" method="post">
                        <div class="mb-3">
                            <label for="titulo" class="form-label">Título</label>
                            <input type="text" class="form-control" id="titulo" name="titulo" value="{titulo}" required>
                        </div>
                        <div class="mb-3">
                            <label for="descricao" class="form-label">Descrição</label>
                            <textarea class="form-control" id="descricao" name="descricao" rows="3">{descricao}</textarea>
                        </div>
                        <div class="mb-3">
                            <label for="categoria_id" class="form-label">Categoria</label>
                            <select class="form-select" id="categoria_id" name="categoria_id">
                                {options}
                            </select>
                        </div>
                        <div class="d-flex gap-2">
                            <button type="submit" class="btn btn-primary">{btn_texto}</button>
                            <a href="/" class="btn btn-outline-secondary">Cancelar</a>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>"""


def render_form_adicionar(categorias):
    html = PAGE_HEADER
    html += '<nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4"><div class="container"><a class="navbar-brand" href="/"><i class="bi bi-check2-square"></i> Gerenciador de Tarefas</a></div></nav>'
    html += _form_tarefa(tarefa=None, categorias=categorias)
    html += PAGE_FOOTER
    return html


def render_form_editar(tarefa, categorias):
    html = PAGE_HEADER
    html += '<nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4"><div class="container"><a class="navbar-brand" href="/"><i class="bi bi-check2-square"></i> Gerenciador de Tarefas</a></div></nav>'
    html += _form_tarefa(tarefa=tarefa, categorias=categorias)
    html += PAGE_FOOTER
    return html
