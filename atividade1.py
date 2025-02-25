employee = [] #Lista para armazenar os funcionários
id_list = 1 #Variável para gerar IDs únicos para os funcionários


#Loop infinito para manter o programa em execução
while True: 
    print("1. Adicionar Funcionário")
    print("2. Listar Funcionário")
    print("3. Atualizar Funcionários")
    print("4. Remover Funcionário")
    print("5. Exibir Funcionário Específico")
    print("6. Sair")
    option = input("Escolha uma opção: ") # Solicita a opção do usuário
        # Adicionar funcionário
    if option == "1":
        name = input("Nome: ")
        age = int(input("Idade: "))
        city = input("Cidade: ")
        state = input("Estado: ")
        school = input("Escolaridade: ")
        job = input("Cargo: ")
        money = float(input("Salário: "))
        employee.append([id_list, name, age, city, state, school, job, money])
        id_list += 1
        print("Funcionário adicionado com sucesso!\n")
        
        # Listar funcionários
    elif option == "2": 
        if not employee:
            print("Nenhum funcionário cadastrado.\n")
        else:
            for f in employee:
                print(f"ID: {f[0]} | Nome: {f[1]} | Idade: {f[2]} | Cidade: {f[3]} | Estado: {f[4]} | Escolaridade: {f[5]} | Cargo: {f[6]} | Salário: R${f[7]:.2f}")
            print()
            
        #Atualizar funcionarios    
    elif option == "3":
        id_update = int(input("ID do funcionário a ser atualizado: "))
        for f in employee:
            if f[0] == id_update:
                f[1] = input("Novo nome: ")
                f[2] = int(input("Nova idade: "))
                f[3] = input("Nova cidade: ")
                f[4] = input("Novo estado: ")
                f[5] = input("Nova escolaridade: ")
                f[6] = input("Novo cargo: ")
                f[7] = float(input("Novo salário: "))
                print("Funcionário atualizado com sucesso!\n")
                break
        else:
            print("Funcionário não encontrado!\n")
        input("Pressione ENTER para voltar ao menu...")
        
        # Remover funcionario    
    elif option == "4":
        id_remove = int(input("ID do funcionário a ser removido: "))
        for f in employee:
            if f[0] == id_remove:
                employee.remove(f)
                print("Funcionário removido com sucesso!\n")
                break
        else:
            print("Funcionário não encontrado!\n")
        input("Pressione ENTER para voltar ao menu...")
        
        # Exibir Funcionario pelo Id Solicitado    
    elif option == "5":
        id_exibir = int(input("ID do funcionário a ser exibido: "))
        for f in employee:
            if f[0] == id_exibir:
                print(f"ID: {f[0]} | Nome: {f[1]} | Idade: {f[2]} | Cidade: {f[3]} | Estado: {f[4]} | Escolaridade: {f[5]} | Cargo: {f[6]} | Salário: R${f[7]:.2f}")
                break
        else:
            print("Funcionário não encontrado!\n")
        input("Pressione ENTER para voltar ao menu...")
        
        # Finalizar Programa    
    elif option == "6":        
            print("Saindo do programa...")
            
            break
        # Controle de erro
    else:
        print("Opção inválida. Tente novamente.")
    
            