nome = input("Digite seu nome!: ")

while nome == "":
    print("============================")
    print ("Você não digitou seu nome!")
    nome = input("Por favor , digite seu nome! ")

print("====================================")
print(f"Hello {nome}, Welcome to the SENAI")
print("====================================")