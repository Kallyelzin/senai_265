def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
preco_mega_caixa = float(input("Qual o preço da mega caixa? "))
print(formatar_real(preco_mega_caixa))