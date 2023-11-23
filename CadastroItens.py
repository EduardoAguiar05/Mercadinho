# Módulo 01

itens = []

def cadastrar_item():
    nome = input("Nome do item: ")
    descricao = input("Descrição do item: ")
    condicao = input("Condição do item: ")

    fotos = input("Anexar fotos (separadas por vírgulas): ")
    fotos = fotos.split(',')

    tipo_acao = input("Escolha o tipo de ação (1 para troca, 2 para doação): ")
    while tipo_acao not in ["1", "2"]:
        print("Opção inválida. Escolha 1 para troca ou 2 para doação.")
        tipo_acao = input("Escolha o tipo de ação (1 para troca, 2 para doação): ")

    if tipo_acao == "1":
        tipo_acao = "Troca"
    else:
        tipo_acao = "Doação"

    item = {
        'nome': nome,
        'descricao': descricao,
        'condicao': condicao,
        'fotos': fotos,
        'tipo_acao': tipo_acao
    }

    itens.append(item)
    print("Item cadastrado com sucesso!")

def listar_itens():
    for i, item in enumerate(itens, 1):
        print(f"Item {i}:")
        print(f"Nome: {item['nome']}")
        print(f"Descrição: {item['descricao']}")
        print(f"Condição: {item['condicao']}")
        print(f"Tipo de Ação: {item['tipo_acao']}")
        print(f"Fotos: {', '.join(item['fotos'])}")
        print("----------------------")

while True:
    print("1. Cadastrar Item")
    print("2. Listar Itens")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_item()
    elif opcao == '2':
        listar_itens()
    elif opcao == '3':
        print('Obrigado e volte sempre!')
        break
    else:
        print("Opção inválida. Tente novamente.")
