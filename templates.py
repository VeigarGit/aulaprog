from typing import List, Any, Dict, Optional


def page_template(title: str, body: str) -> str:
    return f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-..." crossorigin="anonymous" />
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-danger mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">Teste do Gerenciador de Tarefas</a>
        </div>
    </nav>
    <div class="container mb-4">{body}</div>
</body>
</html>
"""


def render_tarefas(tarefas: List[Dict], filtro: Optional[str] = None) -> str:
    filtro_label = "Todas" if not filtro else ("Concluídas" if filtro == "concluida" else "Pendentes")
    rows = ""
    for tarefa in tarefas:
        if tarefa["status"] == "concluida":
            status_badge = "<span class='badge bg-success'>Concluída</span>"
            action_text = "Reabrir"
        elif tarefa["status"] == "em andamento":
            status_badge = "<span class='badge bg-info text-dark'>Em Andamento</span>"
            action_text = "Concluir"
        else:
            # Caso a tarefa esteja com o status "pendente" (atrasada)
            status_badge = "<span class='badge bg-warning text-dark'>Pendente</span>"
            action_text = "Concluir"
        rows += f"""
            <tr>
                <td>{tarefa['tarefa']}</td>
                <td>{tarefa['descricao']}</td>
                <td>{status_badge}</td>
                <td>{tarefa['data_criacao'][:19].replace('T', ' ') if tarefa['data_criacao'] else 'N/A'}</td>
                <td>{tarefa['data_limite'] if tarefa['data_limite'] else 'N/A'}</td>
                <td>{tarefa['data_conclusao'][:19].replace('T', ' ') if tarefa['data_conclusao'] else 'N/A'}</td>
                <td>
                    <a href='/editar?id={tarefa['id'],}' class='btn btn-sm btn-outline-primary'>Editar</a>
                    <a href='/status?id={tarefa['id']}' class='btn btn-sm btn-outline-success'>{action_text}</a>
                    <a href='/deletar?id={tarefa['id']}' class='btn btn-sm btn-outline-danger'>Excluir</a>
                </td>
            </tr>
        """

    body = f"""
        <div class='row'>
            <div class='col-md-6'>
                <div class='card mb-4'>
                    <div class='card-body'>
                        <h5 class='card-title'>Cadastrar nova tarefa</h5>
                        <form action='/tarefas' method='post'>
                            <div class='mb-3'>
                                <label class='form-label'>Título</label>
                                <input type='text' name='tarefa' class='form-control' required />
                            </div>
                            <div class='mb-3'>
                                <label class='form-label'>Descrição</label>
                                <textarea name='descricao' class='form-control' rows='3'></textarea>
                            </div>
                            <div class='mb-3'>
                                <label class='form-label'>Status</label>
                                <select name="status" id="status">
                                    <option value="em andamento">Em andamento</option>
                                    <option value="pendente">Pendente</option>
                                    <option value="concluida">Concluída</option>
                                </select>
                            </div>
                            <div class='mb-3'>
                                <label class='form-label'>Prazo</label>
                                <input type='date' name='data_limite' class='form-control' />
                            </div>
                            <button type='submit' class='btn btn-primary'>Salvar tarefa</button>
                        </form>
                    </div>
                </div>
            </div>




            <div class='col-md-6'>
                <div class='card mb-4'>
                    <div class='card-body'>
                        <h5 class='card-title'>Filtros</h5>
                        <div class='btn-group' role='group'>
                            <a href='/' class='btn btn-outline-secondary'>Todas</a>
                            <a href='/?status=em andamento' class='btn btn-outline-secondary'>Em andamento</a>
                            <a href='/?status=pendente' class='btn btn-outline-secondary'>Pendentes</a>
                            <a href='/?status=concluida' class='btn btn-outline-secondary'>Concluídas</a>
                        </div>
                        <p class='mt-3 mb-0 text-muted'>Mostrando: <strong>{filtro_label}</strong></p>
                    </div>
                </div>
            </div>
        </div>
        <div class='card'>
            <div class='card-body'>
                <h5 class='card-title'>Lista de tarefas</h5>
                <div class='table-responsive'>
                    <table class='table table-striped table-hover'>
                        <thead>
                            <tr>
                                <th>Título</th>
                                <th>Descrição</th>
                                <th>Status</th>
                                <th>Criada em</th>
                                <th>Prazo</th>
                                <th>Concluída em</th>
                            </tr>
                        </thead>
                        <tbody>
                            {rows if rows else '<tr><td colspan="5" class="text-center">Nenhuma tarefa cadastrada.</td></tr>'}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    """
    return page_template("Gerenciador de Tarefas", body)


def render_edita(tarefa: Dict[str, Any]) -> str:
    if not tarefa:
        return page_template("Tarefa não encontrada", "<div class='alert alert-danger'>Tarefa não encontrada.</div>")

    body = f"""
        <div class='card'>
            <div class='card-body'>
                <h5 class='card-title'>Editar tarefa</h5>
                <form action='/editar' method='post'>
                    <input type='hidden' name='id' value='{tarefa['id']}' />
                    <div class='mb-3'>
                        <label class='form-label'>Título</label>
                        <input type='text' name='tarefa' class='form-control' value='{tarefa['tarefa']}' required />
                    </div>
                    <div class='mb-3'>
                        <label class='form-label'>Descrição</label>
                        <textarea name='descricao' class='form-control' rows='4'>{tarefa['descricao']}</textarea>
                    </div>
                    <div class='mb-3'>
                        <label class='form-label'>Status</label>
                        <select name="status" id="status">
                            <option value="em andamento" {{"selected" if tarefa['status'] == "em andamento" else ""}}>Em Andamento</option>
                            <option value="concluida" {{"selected" if tarefa['status'] == "concluida" else ""}}>Concluída</option>
                        </select>
                    </div>
                    <div class='mb-3'>
                        <label class='form-label'>Prazo</label>
                        <input type='date' name='data_limite' class='form-control' value='{tarefa['data_limite']}' />
                    </div>
                    <button type='submit' class='btn btn-primary'>Salvar alterações</button>
                    <a href='/' class='btn btn-secondary ms-2'>Cancelar</a>
                </form>
            </div>
        </div>
    """
    return page_template("Editar Tarefa", body)
