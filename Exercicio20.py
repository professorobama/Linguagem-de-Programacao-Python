# 20) Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

valor1 = int (input("Digite o 1º valor:"))
valor2 = int (input("Digite o 2º valor:"))

if valor1<valor2:
    print("O menor valor corresponde a :{}".format(valor1), "e o maior valor corresponde a :{}".format(valor2))
else:
    print("O menor valor corresponde a :{}".format(valor2), "e o maior valor corresponde a :{}".format(valor1))