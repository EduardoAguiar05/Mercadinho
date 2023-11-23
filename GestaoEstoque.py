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