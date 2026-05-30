procurar = input("Pesquisar peça? ")
estoque = ["Prego", "Porca", "Arruela", "Parafuso", "Mola"]

for i in estoque:
    if i == procurar:
        print("Item em estoque!")
        break
else:
   print("Sem o item no estoque")  