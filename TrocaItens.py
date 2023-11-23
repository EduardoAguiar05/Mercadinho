# Módulo 05

creditos_clientes = {}
catalogo_itens = {
    "Banana": 10,
    "Maçã": 20,
    "Laranja": 15,
    "Maracujá": 30,
    "Melancia": 25
}

def atribuir_creditos():
    cliente = input("Informe o seu nome: ")
    valor_creditos = float(input("Informe o valor dos créditos a serem atribuídos: "))

    if cliente in creditos_clientes:
        creditos_clientes[cliente] += valor_creditos
    else:
        creditos_clientes[cliente] = valor_creditos

    print(f"Créditos atribuídos com sucesso! Créditos totais de {cliente}: {creditos_clientes[cliente]}")

def consultar_creditos(cliente):
    return creditos_clientes.get(cliente, 0)

def visualizar_catalogo():
    
    print('=' * 50)
    print("Catálogo de Itens Disponíveis:")
    for item, valor in catalogo_itens.items():
        print(f"{item}: {valor} créditos")
    print('=' * 50)

def trocar_itens():
    cliente = input("Informe o seu nome: ")
    
    if cliente in creditos_clientes:
        print(f"Saldo atual de créditos de {cliente}: {creditos_clientes[cliente]}")
        
    else:
        print(f"Cliente '{cliente}' não encontrado. Por favor, atribua créditos antes de trocar itens.")
        return

    print('=' * 50)
    visualizar_catalogo()
    print('=' * 50)
    
    itens_para_troca = input("Informe o item desejado para troca: ")
    
    itens_para_troca = [itens_para_troca]

    total_creditos = sum(catalogo_itens.get(item, 0) for item in itens_para_troca)
    
    if creditos_clientes[cliente] >= total_creditos:
        for item in itens_para_troca:
            creditos_clientes[cliente] -= catalogo_itens.get(item, 0)
        print(f"Troca realizada com sucesso! Novo saldo de créditos de {cliente}: {creditos_clientes[cliente]}")
    else:
        print("Saldo de créditos insuficiente para realizar a troca.")

if __name__ == "__main__":
    while True:
        print("Opções:")
        print("1. Atribuir créditos a um cliente")
        print("2. Visualizar catálogo de itens disponíveis")
        print("3. Trocar créditos por item")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            atribuir_creditos()
        elif opcao == "2":
            visualizar_catalogo()
        elif opcao == "3":
            trocar_itens()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")