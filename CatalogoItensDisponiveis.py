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