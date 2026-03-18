# -Adicionar tarefa -Remover tarefa -Listar tarefas -Salvar em arquivo .txt
lista = []

while True:
    try:
        print("\n     LISTA DE TAREFAS\n")
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Listar tarefa(s)")
        print("4 - Salvar lista de tarefas")
        opçao = int(input("\nQual opção você deseja executar? "))

        if opçao == 1:
            tarefa = input("Adicione uma tarefa a sua lista: ")
            lista.append(tarefa)
            print("Tarefa adicionada com sucesso na lista.")

        elif opçao == 2:
            if len(lista) < 1:
                print("Não existe nehnuma tarefa em sua lista.")
            else:     
                while True:
                    remover = input("Qual tarefa da sua lista você deseja remover? ")
                    if remover in lista:
                        lista.remove(remover)
                        print("Tarefa removida.")
                        break
                    elif remover == "nenhum":
                        print("Nenhum item foi removido.")
                        break
                    else:
                        print("Tarefa não encontrada na sua lista. Favor digite corretamente ou digite 'nenhum' para voltar às opções.")    

        elif opçao == 3:
            if len(lista) > 0:
                print("\nTarefas adicionadas a lista:\n")
                for n in lista:
                    print(f"- {n}")
            else:
                print("\nNão existe tarefas adicionadas a sua lista.")        

        elif opçao == 4:
            with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
                for tarefa in lista:
                    arquivo.write(tarefa + "\n")   
            print("Lista salva com sucesso!")
            break

        else:
            print("Essa opção não existe, favor tentar novamente.")    

    except ValueError:
        print("Digite apenas números.")            