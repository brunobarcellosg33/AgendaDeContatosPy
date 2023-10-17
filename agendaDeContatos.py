contatos = []
def criar_contato(nome, telefone):
    contato = {"nome" :nome, "telefone" :telefone}
    contatos.append(contato)
def listar_contatos():
    if not contatos:    
        print("Nenhum contato existente")
    else:
        print("Lista de contatos: ")
        for i, contato in enumerate(contatos):
            print(f"{i+1}. Nome: {contato['nome']}, telefone: {contato['telefone']}") 
def atualizar_contato(indice, nome_novo, telefone_novo):
    if indice >= 0 and indice < len(contatos):
        contatos[indice]["nome"] = nome_novo
        contatos[indice]["telefone"] = telefone_novo
        print("Valores alterados com sucesso")
    else:
        print("Valor passado como índice é inválido")
def excluir_contato(indice):
    if indice >= 0 and indice < len(contatos):
        contato_excluido = contatos.pop(indice)
        print(f"Contato {contato_excluido['nome']} foi excluído com sucesso!")
    else:
        print("índice do valor a ser removido não existe.")

while True:
    print("\nOpções")
    print("1. Criar novo contato")
    print("2. Listar contatos")
    print("3. Atualizar contato")
    print("4. Excluir contato")
    print("5. Sair")

    escolha = input("Digite uma opção: ") 

    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        criar_contato(nome, telefone)
    elif escolha == '2':
        listar_contatos()
    elif escolha == '3':
        listar_contatos()
        indice = int(input("Digite o índice do contato que deseja alterar: ")) -1
        nome_novo = input("Digite o nome a ser alterado: ")
        telefone_novo = input("Digite o telfone a ser alterado: ")
        atualizar_contato(indice, nome_novo, telefone_novo)
    elif escolha == '4':
        listar_contatos()  
        indice = int(input("Digite o índice do contato que deseja excluir: ")) -1
        excluir_contato(indice) 
    elif escolha == '5':
        print("Obrigado por usar o programa, até breve!")
        break
    else:
        print("Escolha inválida, digite novamente.")