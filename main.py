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

# Módulo 04

catalogo_itens = {
    "Banana": 10,
    "Maçã": 20,
    "Laranja": 15,
    "Maracujá": 30,
    "Melancia": 25
}
                  
def visualizar_catalogo():
    
    print('=' * 50)
    print("Catálogo de Itens Disponíveis:")
    for item, valor in catalogo_itens.items():
        print(f"{item}: {valor} créditos")
    print('=' * 50)

# Módulo 05

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

# Módulo 07

import csv

class Mercado:
    def __init__(self):
        self.itens_cadastrados = 0
        self.itens_avaliados = 0
        self.itens_doados = 0


    def cadastrar_item(self):
        self.itens_cadastrados += 1


    def avaliar_item(self):
        self.itens_avaliados += 1


    def doar_item(self):
        self.itens_doados += 1


    def gerar_relatorio(self, formato='txt'):
        relatorio = f"Relatório do Mercadinho\n"
        relatorio += f"Número de itens cadastrados: {self.itens_cadastrados}\n"
        relatorio += f"Número de itens avaliados: {self.itens_avaliados}\n"
        relatorio += f"Número de itens doados: {self.itens_doados}\n"

        if formato == 'txt':
            self.exportar_txt(relatorio)
        elif formato == 'csv':
            self.exportar_csv(relatorio)


    def exportar_txt(self, relatorio):
        with open('relatorio_mercadinho.txt', 'w') as arquivo:
            arquivo.write(relatorio)
        print("Relatório exportado para relatorio_mercadinho.txt")


    def exportar_csv(self, relatorio):
        with open('relatorio_mercadinho.csv', 'w', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            linhas = relatorio.split('\n')
            for linha in linhas:
                if linha:
                    escritor_csv.writerow(linha.split(':'))
        print("Relatório exportado para relatorio_mercadinho.csv")


if __name__ == "__main__":
    mercadinho = Mercado()
    mercadinho.cadastrar_item()
    mercadinho.avaliar_item()
    mercadinho.doar_item()

    mercadinho.gerar_relatorio(formato='txt')
    mercadinho.gerar_relatorio(formato='csv')

# Módulo 08 - Gestão de estoque de produtos à venda

produtos = {}
produtos_atualizados = {}

def cadastrar_produto(codigo, nome, categoria, preco, quantidade):
    
    if codigo not in produtos:
        produtos[codigo] = {'nome': nome, 'categoria': categoria, 'preco': preco, 'quantidade': quantidade}
        print(f"Produto '{nome}' cadastrado com sucesso!")
        
    else:
        produtos[codigo]['quantidade'] += quantidade 
        print(f"Quantidade de '{nome}' atualizada com sucesso!")

def vender_produto(codigo, quantidade_vendida):
    
    if codigo in produtos:
        produto = produtos[codigo]
        
        if produto['quantidade'] >= quantidade_vendida:
            produto['quantidade'] -= quantidade_vendida
            print(f"{quantidade_vendida} unidades de '{produto['nome']}' vendidas com sucesso!")
            
        else:
            print("Quantidade insuficiente em estoque para realizar a venda.")
    else:
        print("Produto não encontrado. Verifique o código.")

def repor_estoque(codigo, quantidade_reposta):
    
    if codigo in produtos:
        produto = produtos[codigo]
        produto['quantidade'] += quantidade_reposta
        print(f"{quantidade_reposta} unidades de '{produto['nome']}' adicionadas ao estoque.")
        
    else:
        print("Produto não encontrado. Verifique o código.")

def atualizar_produto(codigo, nome=None, categoria=None, preco=None, quantidade=None):
    
    if codigo in produtos:
        produto = produtos[codigo]
        
        if nome is not None:
            produto['nome'] = nome
            
        if categoria is not None:
            produto['categoria'] = categoria
            
        if preco is not None:
            produto['preco'] = preco
            
        if quantidade is not None:
            produto['quantidade'] = quantidade
            
        produtos_atualizados[codigo] = produto 
        print(f"Informações do produto '{produto['nome']}' atualizadas com sucesso!")
        
    else:
        print("Produto não encontrado. Verifique o código.")

def listar_produtos():
    
    print("\nLista de produtos:")
    print('=' * 125)
    
    if not produtos:
        print("Nenhum produto cadastrado.")
        
    else:
        print("{:<10} {:<20} {:<15} {:<10} {:<15}".format("Código", "Nome", "Categoria", "Preço", "Quantidade"))
        for codigo, produto in produtos.items():
            print("{:<10} {:<20} {:<15} R${:<9.2f} {:<15}".format(codigo, produto['nome'], produto['categoria'], produto['preco'], produto['quantidade']))
    print('=' * 125)

def listar_produtos_atualizados():
    
    print("\nLista de produtos atualizados:")
    print('=' * 125)
    
    if not produtos_atualizados:
        print("Nenhum produto atualizado.")
        
    else:
        print("{:<10} {:<20} {:<15} {:<10} {:<15}".format("Código", "Nome", "Categoria", "Preço", "Quantidade"))
        for codigo, produto in produtos_atualizados.items():
            print("{:<10} {:<20} {:<15} R${:<9.2f} {:<15} ".format(codigo, produto['nome'], produto['categoria'], produto['preco'], produto['quantidade']))
    print('=' * 125)

def vender_produtos():
    
    while True:
        try:
            codigo_venda = int(input('\nDigite o código do produto a ser vendido: '))
            break
        except ValueError:
            print("Por favor, digite um número para o código do produto.")

    while True:
        try:
            quantidade_vendida = float(input('\nDigite a quantidade a ser vendida: '))
            break
        except ValueError:
            print("Por favor,a quantidade a ser vendida.")
            
    vender_produto(codigo_venda, quantidade_vendida)

while True:
    print("\nOpções:")
    print("1. Adicionar produto")
    print("2. Ver estoque de produtos")
    print("3. Vender produtos")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        
        while True:
            try:
                codigo = int(input('\nDigite o código do produto a ser cadastrado: '))
                break  
            except ValueError:
                print("Por favor, digite um número para o código do produto.")

        while True:
            try:
                nome = str(input('\nDigite o nome do produto a ser cadastrado: '))
                break  
            except ValueError:
                print("Por favor, digite um nome para o produto.")

        while True:
            try:
                categoria = str(input('\nDigite a categoria do produto a ser cadastrado: '))
                break  
            except ValueError:
                print("Por favor, digite uma categoria para o produto.")

        while True:
            try:
                quantidade = float(input('\nDigite a quantidade do produto a ser cadastrado (Pacotes): '))
                break
            except ValueError:
                print("Por favor, digite a quantidade correta do produto.")
                
        while True:
            try:
                preco = float(input('\nDigite o valor unitário do produto a ser cadastrado: '))
                break  
            except ValueError:
                print("Por favor, digite um número para o preço do produto.")
                
        cadastrar_produto(codigo, nome, categoria, preco, quantidade)

        listar_produtos()
            
        while True:
            print('\nDeseja atualizar algum produto?\n')
            print('1. Sim ')
            print('2. Não')

            opcao = input('\n-> Escolha a opção desejada: ')

            if opcao == '2':
                print()
                break
                
            elif opcao == '1':
                
                while True:
                    try:
                        codigo_atualizar = int(input('\nDigite o código do produto a ser atualizado: '))
                        break
                    except ValueError:
                        print("Por favor, digite um número para o código atualizado do produto.")

                while True:
                    try:
                        nome_atualizar = str(input('\nDigite o nome do produto a ser atualizado: '))
                        break
                    except ValueError:
                        print("Por favor, digite o nome atualizado do produto.")

                while True:
                    try:
                        categoria_atualizar = str(input('\nDigite a nova categoria do produto: '))
                        break
                    except ValueError:
                        print("Por favor, digite uma categoria para atualizar o produto.")

                while True:
                    try:
                        quantidade_atualizar = float(input('\nDigite a nova quantidade do produto: '))
                        break
                    except ValueError:
                        print("Por favor, digite a quantidade correta atualizada do produto.")

                while True:
                    try:
                        preco_atualizar = float(input('\nDigite o novo valor unitário do produto: '))
                        break
                    except ValueError:
                        print("Por favor, digite um número para o preço atualizado do produto.")

                atualizar_produto(codigo_atualizar, nome=nome_atualizar, categoria=categoria_atualizar, preco=preco_atualizar, quantidade=quantidade_atualizar)

                listar_produtos_atualizados()

    elif escolha == "2":
        listar_produtos()
        
    elif escolha == "3":
        vender_produtos()

    elif escolha == "4":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Escolha novamente.")

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

# Módulo 10 - Relatórios Estatísticos

total_vendas = 0
total_itens_trocados = 0
dados_produtos = {}

# Dados do gerente
def realizar_login():
    usuario_correto = "Ailton"
    senha_correta = "271204"

    while True:
        try:
            usuario_input = input("Usuário: ")
            senha_input = input("Senha: ")

            if usuario_input == usuario_correto and senha_input == senha_correta:
                print("Olá, Ailton. Tenha um bom expediente!")
                break  # Saia do loop se a autenticação for bem-sucedida
            else:
                print("Usuário ou senha incorretos. Tente novamente.")
        except ValueError:
            print("Por favor, digite o usuário e senha corretamente!")

realizar_login()  

while True:
    try:
        total_vendas = int(input("Digite o total de vendas: "))
        if total_vendas < 0:
            print("O total de vendas deve ser um número positivo. Tente novamente.")
        else:
            break
    except ValueError:
        print("Por favor, digite um número válido para o total de vendas.")

while True:
    produto = input("Digite o nome do produto mais popular (ou 'sair' para encerrar): ")
    if produto.lower() == 'sair':
        break 
        
    while True:
        try:
            quantidade_vendida = int(input(f"Digite a quantidade vendida para {produto}: "))
            if quantidade_vendida < 0:
                print("A quantidade vendida deve ser um número positivo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido para a quantidade vendida.")

    dados_produtos[produto] = {'quantidade_vendida': quantidade_vendida}
    total_vendas += quantidade_vendida

while True:
    try:
        total_itens_trocados = int(input("Digite o total de itens trocados: "))
        if total_itens_trocados < 0:
            print("O total de itens trocados deve ser um número positivo. Tente novamente.")
        else:
            break
    except ValueError:
        print("Por favor, digite um número válido para o total de itens trocados.")