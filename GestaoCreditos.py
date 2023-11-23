# Módulo 03

creditos_clientes = {}

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