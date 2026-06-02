usuarios = [
    ["Katakiriamoto", "katakiriamoto@gmail.com", 36],
    ["V3rme", "v3rme@gmail.com", 16],
    ["Peneu", "peneu@gmail.com", 26],
    ["Ryo", "devryo@gmail.com", 46]
]
# print(usuarios)
usuario1 = usuarios[0]
nome_u1 = usuarios[0][0]
gmail_u1 = usuarios[0][1]
idade_u1 = usuarios[0][2]

usuario2 = usuarios[1]
nome_u2 = usuarios[1][0]
gmail_u2 = usuarios[1][1]
idade_u2 = usuarios[1][2]

usuario3 = usuarios[2]
nome_u3 = usuarios[2][0]
gmail_u3 = usuarios[2][1]
idade_u3 = usuarios[2][2]

usuario4 = usuarios[3]
nome_u4 = usuarios[3][0]
gmail_u4 = usuarios[3][1]
idade_u4 = usuarios[3][2]
print("Procure entre:")
print("usuario 1 / usuario 2 / usuario 3 / usuario 4")
search = input("Qual usuario você está procurando?")
while True:
    search == "usuario 1":

        print("Informações do primeiro usuario\n")
        print(f"Nome usuario 1: {nome_u1}")
        print(f"Gmail usuario 1: {gmail_u1}")
        print(f"Idade usuario 1: {idade_u1}")

    elif search == "usuario 2":

        print("Informações do seguundo usuario\n")
        print(f"Nome usuario 2: {nome_u2}")
        print(f"Gmail usuario 2: {gmail_u2}")
        print(f"Idade usuario 2: {idade_u2}")

    elif search == "usuario 3":

        print("Informações do terceiro usuario\n")
        print(f"Nome usuario 3: {nome_u1}")
        print(f"Gmail usuario 3: {gmail_u1}")
        print(f"Idade usuario 3: {idade_u1}")

    elif search == "usuario 4":

        print("Informações do quarto usuario\n")
    print(f"Nome usuario 4: {nome_u1}")
    print(f"Gmail usuario 4: {gmail_u1}")
    print(f"Idade usuario 4: {idade_u1}")
else:
    print("Usuario não encontrado!")

if
