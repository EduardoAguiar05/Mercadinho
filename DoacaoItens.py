# Módulo 06

import datetime

class Mercadinho1:

    def __init__(self):
        self.inventario = {}
        self.historico_doacoes = []


    def adicionar_item(self, nome, quantidade):

        if nome in self.inventario:
            self.inventario[nome] += quantidade

        else:
            self.inventario[nome] = quantidade


    def realizar_doacao(self, nome, quantidade):

        if nome in self.inventario and self.inventario[nome] >= quantidade:
            self.inventario[nome] -= quantidade

            if self.inventario[nome] > 0:
                doacao = {
                    'nome': nome,
                    'quantidade': quantidade,
                    'data': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }

                self.historico_doacoes.append(doacao)

                print(f"\n{quantidade} unidades de {nome} foram doadas com sucesso!")

            else:
                print(f"\nTodas as unidades de {nome} foram doadas com sucesso! Removendo do inventário...\n")

                del self.inventario[nome]
        else:
            print("\nProduto não disponível para doação.\n")


    def exibir_inventario(self):
        print("\nInventário:")

        for item, quantidade in self.inventario.items():
            print(f"\n-> {item}: {quantidade} unidades")
        print()


    def exibir_historico_doacoes(self):
        print("\nHistórico de Doações:\n")

        for doacao in self.historico_doacoes:
            print(f"{doacao['data']} - {doacao['quantidade']} unidades de {doacao['nome']}")


mercadinho = Mercadinho1()

while True:

    print("1 - Adicionar item ao inventário")
    print("2 - Realizar doação")
    print("3 - Exibir inventário")
    print("4 - Exibir histórico de doações")
    print("5 - Sair")

    escolha = input("\nEscolha uma opção: ")

    if escolha == "1":
        nome = input("\nDigite o nome do produto: ")
        quantidade = int(input("Digite a quantidade a adicionar: "))

        mercadinho.adicionar_item(nome, quantidade)

        print("\nProduto adicionado com sucesso!\n")

    elif escolha == "2":
        nome = input("\nDigite o nome do produto a ser doado: ")
        quantidade = int(input("Digite a quantidade a doar: "))

        mercadinho.realizar_doacao(nome, quantidade)

    elif escolha == "3":
        mercadinho.exibir_inventario()

    elif escolha == "4":
        mercadinho.exibir_historico_doacoes()

    elif escolha == "5":
        break

    else:
        print("\nOpção inválida! Tente novamente.\n")