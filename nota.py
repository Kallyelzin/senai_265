n1 = float(input("Qual sua nota no 1 Tri? "))
n2 = float(input("Qual sua nota no 2 Tri? "))
n3 = float(input("Qual sua nota no 3 Tri? "))
n4 = float(input("Qual sua nota no 4 Tri? "))

soma = n1 + n2 + n3 + n4
media = soma / 4.0 

if media >= 9:
    print("Good, You're a good men")

elif media >= 7:
    print("Good!")

else:
    print("Tomatos in you'r head")