## criar lista estilo playlist com 10 musicas, usar laco para exibir toda a lista

playlist1 = ["Just the way you are", "Ô queiroz", "Asleep in space", "HERTBROKEN (Oblivion)", "Me desculpa Flauta", "I thought your face today", "Resurrections", "nuts", "see you again", "innocence daniel caesar"]
print(playlist1)
search = input("Qual musica Você esta procurando?: ")

for i in playlist1:
    if i == search:
        print("Musica na playlist!")
        break
    else:
        print("Esta musica não foi encontrada nessa playlist")
        