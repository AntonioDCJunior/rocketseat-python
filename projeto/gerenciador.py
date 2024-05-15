def adicionar_tarefa(tarefas, nome_tarefa):    
    #Tarefa: nome da tarefa
    #Completada: indicar se a tarefa foi completada ou não
    tarefa = {"tarefa": nome_tarefa, "completada": False} #Usando dicionário pois serão usadas mais de uma informação que são: nome da tarefa e se ela foi completada ou não
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    print("\n Lista de tarefas")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa inválido!")    
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"O status da tarefa {indice_tarefa} foi atualizado para COMPLETADA!")
    return

def deletar_tarefa(tarefas, indice_tarefa):
    deletar_indice_tarefa = int(indice_tarefa) - 1
    tarefas[deletar_indice_tarefa]
    return

tarefas = [] #É iniciada uma lista vazia para ser preenchida conforme a opção escolhida
while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar uma Tarefa")
    print("2. Ver uma Tarefa")
    print("3. Atualizar uma Tarefa")
    print("4. Completar uma Tarefa")
    print("5. Deletar Tarefas completadas")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_tarefa = input("Adicione uma tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    
    if escolha == "2":
        ver_tarefas(tarefas)

    if escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Informe o numero da tarefa para ser atualizada: ")
        novo_nome = input("Informe o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    if escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Informe o nÚmero da tarefa para ser completada: ")
        #novo_status = input("A tarefa foi completada? ")
        completar_tarefa(tarefas, indice_tarefa)
        
    elif escolha == "6":
        break

    #else:
    #    print("Opção inválida, tente novamente!")