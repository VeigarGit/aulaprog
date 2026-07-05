from controllers.tarefas_controller import TarefaController
from repositorios.sqlite_repo import SqliteTarefaRepository

def entrada_usuario():
    escolha = input(
        "O que deseja fazer?\n"
        "1 - Criar Tarefa\n"
        "2 - Remover Tarefa\n"
        "3 - Concluir Tarefa\n"
        "4 - Pender Tarefas\n"
        "5 - Listar Tarefas\n"
        "6 - Filtrar Tarefas por Status\n"
        "7 - Finalizar : "
    )
    return escolha


repo = SqliteTarefaRepository("MANAGER")
action = TarefaController(repo)

while True:
    print("\nBem-vindo ao sistema de Gerenciamento de Tarefas")

    opcao = entrada_usuario()

    match opcao:
        case "1":
            print("Criar tarefa :")
            tarefa = input("Qual Tarefa Deseja Criar : ")
            action.criar_tarefa(tarefa)

        case "2":
            tarefa = input("Qual Tarefa Deseja Remover [Apenas por Id] : ")
            action.remover_tarefa(tarefa)

        case "3":
            tarefa = input("Qual Tarefa Deseja Concluir [Apenas por Id] : ")
            action.concluir_tarefa(tarefa)

        case "4":
            tarefa = input("Qual Tarefa Deseja deixar como Pendente [Apenas por Id] : ")
            action.pender_tarefa(tarefa)

        case "5":
            print("Listar Todas as Tarefas.")
            lista = action.listar_tarefas()
            print("===== Atualmente os Itens da Sua Lista são ====")
            for item in lista:
                print(item)

        case "6":
            tarefa = input("Por qual Status Deseja Filtrar a Lista de Tarefas [Pendente[1]/Concluída[2]] : ")

            if tarefa != "1" and tarefa != "2":
                print("Valor incorreto, tente novamente")
                tarefa = input("Por qual Status Deseja Filtrar a Lista de Tarefas [Pendente[1]/Concluída[2]] : ")

            if tarefa == "1":
                lista = action.listar_por_status("PENDENTE")

            if tarefa == "2":
                lista = action.listar_por_status("CONCLUIDA")
            print("===== Atualmente os Itens da Sua Lista são ====")
            for item in lista:
                print(item)

        case "7":
            print("Encerrando programa.")
            break

        case _:
            print("Opção inválida")