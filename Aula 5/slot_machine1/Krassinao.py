import random

simbolos = ["👀", "🥵", "🥱", "🤓", "😍"]
saldo = 20.0
print("=== Krassinao do senai ===\n")
while saldo >= 2:
    input("\n Pressione ENTER para girar (custo R$2)")
    saldo -= 2

    resultado = [random.choice(simbolos) for i in range(3)]
    print(" | ".join(resultado))

    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        print(f" JACKPOTTT!!!! você ganhou R${premio}! ")

        print(f"Saldo atual: R${saldo:.2f}")
    elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
        premior = 10
        saldo += premior
        print(f"Good! Você ganhou R${premior}")

        print(f"Saldo atual: R${saldo:.2f}")
    else: 
        print("Não foi dessa vez...😢")        

        print(f"Saldo atual: R$ {saldo:.2f}")