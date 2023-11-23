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