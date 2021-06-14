# 13) Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste
#  aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5.
# Fórmula para o cálculo da média final é:
# mediafinal= (n1 * 2 + n2 * 3 + n3 * 5)/10

nota1=float(input("Digite o valor da 1º Nota :"))
nota2=float(input("Digite o valor da 1º Nota :"))
nota3=float(input("Digite o valor da 1º Nota :"))

media= (nota1 * 2 + nota2 * 3 + nota3 * 5)/10

print("O valor da média poderada corresponde a : {}".format(media))