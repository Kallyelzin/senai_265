print("==== conversor de peso (Peso 🔄 arroba) ====")

peso = float(input("Digite o peso? "))
unidade = input("Em K (quilos) ou em A (arrobas)? ")

if unidade == "K":
    arrobas = peso / 15
    print(f"{peso} kg = {arrobas:.2f} arrobas")
elif unidade == "A":
    quilos = peso * 15
    print(f"{peso} arrobas = {quilos:.2f} kg")
else:
    print("Unidade inválida!")