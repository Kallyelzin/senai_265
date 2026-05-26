programa
{
	
	funcao inicio()
	{
	real n1, n2, n3, n4
	real soma , media 
	cadeia resultado

	escreva("Nota 1 Tri: ")
	leia(n1)
	escreva("Nota 2 Tri: ")
	leia(n2)
	escreva("Nota 3 Tri: ")
	leia(n3)
	escreva("Nota 4 Tri: ")
	leia(n4)

	soma = n1 + n2 +n3 +n4
	media = soma / 4.0

	se (media >= 9)
	{
		resultado = "Very Good, you're a good men"
	}	
	senao  se (media >= 7)
	{
		resultado = "Good"
	}
	senao
	{
		resultado = "Tomatos in you'r head"
	}

	escreva("Nota 1:", n1, "\n")
	escreva("Nota 2:", n2, "\n")
	escreva("Nota 3", n3, "\n")
	escreva("Nota 4", n4, "\n")
	escreva("media: ", media, "\n")
	escreva("resultado: ", resultado)
	
	}
} 

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 296; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */