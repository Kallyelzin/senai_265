desconto = input("Você é um estudante? ")
idoso = input("Qual sua idade? ")

if desconto == "sim" or idoso >= 60:
    print("Parabéns você ganhou um desconto!!")
else:
    print("Você não tem desconto!")