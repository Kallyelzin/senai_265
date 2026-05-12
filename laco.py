procurar = input("Pesquisar peça: ")
estoque = ["Prego", "Arruela", "Porca", "Parafuso", "Mola",]
for item in estoque:
    if item == procurar:
        print("Item encontrado no estoque!")
        break #interrompe o laço imediatamente
else:
    print("Item não encontrado após varredura completa!")