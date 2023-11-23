# Módulo 09 

from datetime import datetime

class Mercadinho:
    def __init__(self):
        self.vendas = []


    def realizar_venda(self, data, categoria, valor):
        venda = {
            'data': data,
            'categoria': categoria,
            'valor': valor
        }
        self.vendas.append(venda)


    def balanco_vendas(self, data_inicio=None, data_fim=None, categoria=None):
        vendas_filtradas = self.vendas

        if data_inicio:
            vendas_filtradas = [venda for venda in vendas_filtradas if venda['data'] >= data_inicio]

        if data_fim:
            vendas_filtradas = [venda for venda in vendas_filtradas if venda['data'] <= data_fim]

        if categoria:
            vendas_filtradas = [venda for venda in vendas_filtradas if venda['categoria'] == categoria]

        return vendas_filtradas

mercadinho = Mercadinho()


while True:
    data_str = input("\nDigite a data da venda (Ano-Mês-Dia) ou 'sair' para encerrar: ")

    if data_str.lower() == 'sair':
        break

    try:
        data = datetime.strptime(data_str, '%Y-%m-%d')

    except ValueError:
        print("\nFormato de data inválido! Por favor, digite a data no formato correto.\n")

        continue

    categoria = input("\nDigite a categoria do produto: ")
    valor = float(input("Digite o valor da venda: "))

    mercadinho.realizar_venda(data, categoria, valor)

data_inicio = input("\nDigite a data de início para o balanço (Ano-Mês-Dia): ")
data_fim = input("Digite a data de fim para o balanço (Ano-Mês-Dia): ")
categoria = input("Digite a categoria para filtrar o balanço (Deixe em branco para não filtrar): ")

try:
    data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d') if data_inicio else None
    data_fim = datetime.strptime(data_fim, '%Y-%m-%d') if data_fim else None

except ValueError:
    print("\nFormato de data inválido! Por favor, digite as datas no formato correto.\n")
    exit()

balanco = mercadinho.balanco_vendas(data_inicio, data_fim, categoria)

print("\nBalanço de Vendas:")

if not balanco:
    print("\nNenhuma venda encontrada no período especificado.")

else:
    for venda in balanco:
        print(f"Data: {venda['data']}, Categoria: {venda['categoria']}, Valor: {venda['valor']}")