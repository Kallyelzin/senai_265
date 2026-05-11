print("==== CALCULADORA ====")

n1 = float(input("Qual o primeiro valor? "))
op = input("Qual o operador escolhido? +|-|/|* ")
n2 = float(input("Qual o segundo valor? "))

if op == "+":
    resultado1 = n1 + n2
    print(resultado1)
elif op == "-":
    resultado2 =  n1 - n2
    print(resultado2)
elif op == "/":
    if n2 == 0:
        print("Qualquer numero dividido por zero é 0")
    else:
      resultado3 = n1 / n2
      print(resultado3)
elif  op == "*":
    resultado4 = n1 * n2
    print(resultado4)
else:
   print("Operador inexistente!!")