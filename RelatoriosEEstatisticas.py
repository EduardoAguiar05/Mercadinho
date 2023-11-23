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