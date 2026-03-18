lista = []
try:
    while True:

        print("\nCADASTRAR ALUNOS\n")
        print("1 - Cadrastrar aluno")
        print("2 - Ver lista de alunos")
        print("3 - Média da turma")
        print("4 - Aluno com a maior nota")
        print("5 - Aluno com a menor nota")
        print("6 - Alunos aprovados")
        print("7 - Salvar dados dos alunos\n")
        opçao = int(input("-> "))
        print("")

        if opçao == 1:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            nota = float(input("Digite a nota do aluno: "))

            aluno = {"nome": nome,
                    "idade": idade,
                    "nota": nota
                    }
            lista.append(aluno)
            print("Aluno cadastrado com sucesso.")

        elif opçao == 2:
            if len(lista) > 0:
                for aluno in lista:
                    print(f"Nome: {aluno['nome']} --- Idade: {aluno['idade']} --- Nota: {aluno['nota']}")
            else:
                 print("Nenhum aluno cadastrado.")

        elif opçao == 3:
            if not lista:
                print("Nenhum aluno cadastrado.")
            else:
                divisor = len(lista)
                soma = sum(aluno['nota'] for aluno in lista)
                media = soma / divisor
                print(f"Média da turma: {media}")

        elif opçao == 4: 
            if not lista:
                print("Nenhum aluno cadastrado.")
            else:    
                maior = max(lista, key=lambda aluno: aluno['nota'])
                print(f"Auno - {maior['nome']} | Nota - {maior['nota']}")

        elif opçao == 5:
            if not lista:
                print("Nenhum aluno cadastrado.")
            else:
                menor = min(lista, key=lambda aluno: aluno['nota'])
                print(f"Aluno - {menor['nome']} | Nota: {menor['nota']}")

        elif opçao == 6:
            if not lista:
                print("Nenhum aluno cadastrado.")
            else:    
                for aluno in lista:
                    if aluno['nota'] >= 7:
                        print("Alunos aprovados:\n")
                        print(f"Aluno: {aluno['nome']} | Nota: {aluno['nota']}")      

        elif opçao == 7:
            if not lista:
                print("Nenhum aluno para salvar.")
            else:
                with open("alunos.txt", "a") as arquivo:
                    for aluno in lista:
                        arquivo.write(f"{aluno['nome']} - {aluno['idade']} - {aluno['nota']}\n")
            print("Dados salvos com sucesso.")           
                         
        else:
            print("Digite uma opção válida.")     

except ValueError:
        print("Digite apenas números.")