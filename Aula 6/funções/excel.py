def se(condicao, valor_verdadeiro, valor_falso):
    
    return valor_verdadeiro if condicao else valor_falso
alunos = [
    ("Katakiriamoto", 67),
    ("V3rme", 92),
    ("Peneu", 20),
    ("Ryo", 99)
]

print(f"{'aluno':15} {'nota':>6} {'situacao':^12}")
print("-" * 38)
print("\n ===== Boletin ====")

for nome, nota in alunos:
    situacao = se(nota >= 70, "APROVADO", se(nota >= 50, "RECUPERAÇÃO", "REPROVADO"))
    
    print(f"{nome:15} {nota:>6} {situacao:^12}")
aprovados = 0
recupercao = 0
reprovados = 0

for nome, nota in alunos:
    situacao = se(nota >= 70, "APROVADO", se(nota >= 50, "RECUPERAÇÃO", "REPROVADO"))
    
    if situacao == "APROVADO":
        aprovados +=1
    elif situacao == "RECUPERAÇÃO": 
        recupercao +=1
    else:
        reprovados +=1   
print(f"Total de APROVADOS: {aprovados}")
print(f"Total de RECUPERAÇÃO: {recupercao}")
print(f"Total de REPROVADOS: {reprovados}")
