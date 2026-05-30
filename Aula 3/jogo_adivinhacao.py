import random
print("=== 🧻 ADIVINHE UM NUMERO 🧻 ===")
secreto = random.randint(1, 100)
tentativas = 0
palpites = 0
while palpites != secreto:
    print("Adivinhe um numero de 1-100")
    palpites = int(input("Qual seu palpite? "))
    tentativas += 1
    if palpites < secreto:
        print("Valor Baixo!")
    elif palpites > secreto:
        print("Valor Alto!")
    else:
        print(f"💸JACKPOT💸 com {tentativas} tentativas")
