def estatiscas(*numeros):
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    print(f"Total: {total} | Média: {media} | Máximo: {maximo} | Mínimo: {minimo}")

estatiscas(59, 68, 80, 90, 46)
estatiscas(70, 89, 49)
#listas
lista = [80, 90, 95]
estatiscas(*lista)