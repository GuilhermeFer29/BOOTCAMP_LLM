import json
import os

# Nome do arquivo para salvar os funcionários
FILENAME = "funcionarios.json"

# Função para carregar os funcionários do arquivo JSON
def carregar_dados():
    if os.path.exists(FILENAME):  # Verifica se o arquivo existe
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)  # Carrega os dados
    return []  # Retorna uma lista vazia se o arquivo não existir

# Função para salvar os funcionários no arquivo JSON
def salvar_dados():
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(employee, file, indent=4, ensure_ascii=False)  # Salva os dados

# Carrega os funcionários ao iniciar o programa
employee = carregar_dados()
id_list = max([f["id"] for f in employee], default=0) + 1  # Define o próximo ID

while True:
    print("\n1. Adicionar Funcionário")
    print("2. Listar Funcionários")
    print("3. Atualizar Funcionário")
    print("4. Remover Funcionário")
    print("5. Exibir Funcionário Específico")
    print("6. Sair")
    option = input("Escolha uma opção: ")

    if option == "1":
        name = input("Nome: ")
        age = int(input("Idade: "))
        city = input("Cidade: ")
        state = input("Estado: ")
        school = input("Escolaridade: ")
        job = input("Cargo: ")
        money = float(input("Salário: "))

        employee.append({
            "id": id_list, "nome": name, "idade": age, "cidade": city,
            "estado": state, "escolaridade": school, "cargo": job, "salario": money
        })
        id_list += 1
        salvar_dados()  # Salva no arquivo JSON
        print("Funcionário adicionado com sucesso!\n")

    elif option == "2":
        if not employee:
            print("Nenhum funcionário cadastrado.\n")
        else:
            for f in employee:
                print(f"ID: {f['id']} | Nome: {f['nome']} | Idade: {f['idade']} | Cidade: {f['cidade']} | "
                      f"Estado: {f['estado']} | Escolaridade: {f['escolaridade']} | Cargo: {f['cargo']} | "
                      f"Salário: R${f['salario']:.2f}")
        input("Pressione ENTER para voltar ao menu...")

    elif option == "3":
        id_update = int(input("ID do funcionário a ser atualizado: "))
        for f in employee:
            if f["id"] == id_update:
                f["nome"] = input("Novo nome: ")
                f["idade"] = int(input("Nova idade: "))
                f["cidade"] = input("Nova cidade: ")
                f["estado"] = input("Novo estado: ")
                f["escolaridade"] = input("Nova escolaridade: ")
                f["cargo"] = input("Novo cargo: ")
                f["salario"] = float(input("Novo salário: "))
                salvar_dados()  # Salva no arquivo JSON
                print("Funcionário atualizado com sucesso!\n")
                break
        else:
            print("Funcionário não encontrado!\n")
        input("Pressione ENTER para voltar ao menu...")

    elif option == "4":
        id_remove = int(input("ID do funcionário a ser removido: "))
        for f in employee:
            if f["id"] == id_remove:
                employee.remove(f)
                salvar_dados()  # Salva no arquivo JSON
                print("Funcionário removido com sucesso!\n")
                break
        else:
            print("Funcionário não encontrado!\n")
        input("Pressione ENTER para voltar ao menu...")

    elif option == "5":
        id_exibir = int(input("ID do funcionário a ser exibido: "))
        for f in employee:
            if f["id"] == id_exibir:
                print(f"ID: {f['id']} | Nome: {f['nome']} | Idade: {f['idade']} | Cidade: {f['cidade']} | "
                      f"Estado: {f['estado']} | Escolaridade: {f['escolaridade']} | Cargo: {f['cargo']} | "
                      f"Salário: R${f['salario']:.2f}")
                break
        else:
            print("Funcionário não encontrado!\n")
        input("Pressione ENTER para voltar ao menu...")

    elif option == "6":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
