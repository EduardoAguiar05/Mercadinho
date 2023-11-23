# Módulo 02

class ItemAvaliacao:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.pontuacao = 0

def avaliar_itens(itens):
    for item in itens:
        print(f"Avaliando o item: {item.nome} - {item.descricao}")
        condicao = int(input("Por favor, avalie a condição do item (1 a 10, sendo 10 o melhor): "))
        item.pontuacao = condicao

def classificar_itens(itens):
    for item in itens:
        if item.pontuacao >= 7:
            item.classificacao = "Aprovado para Troca ou Doação"
        else:
            item.classificacao = "Não Aprovado"

def mostrar_resultados(itens):
    for item in itens:
        print(f"Item: {item.nome} - {item.descricao}")
        print(f"Pontuação: {item.pontuacao}")
        print(f"Classificação: {item.classificacao}")
        if item.classificacao == "Não Aprovado":
            justificativa = input("Por favor, forneça uma justificativa para a não aprovação: ")
            print(f"Justificativa: {justificativa}")

def main():
    itens = [ItemAvaliacao("Item 1", "Descrição do Item 1"),
             ItemAvaliacao("Item 2", "Descrição do Item 2"),
             ]

    avaliar_itens(itens)

    classificar_itens(itens)

    mostrar_resultados(itens)

if __name__ == "__main__":
    main()