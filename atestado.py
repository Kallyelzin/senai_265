idade = int(input("Qual a idade? "))
condicao = input("Qual a condição fisica? ")
letal = input("Necessario um atestado? ")

if idade >= 18 and (condicao or letal):
    print("OK voce ganhou")
else:
    print("Não")