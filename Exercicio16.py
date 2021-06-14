# As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
# compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
# escreva o custo total da compra.

macas = int(input("Digite a quantidade de maças compradas: "))
if macas<12: 
    valorTotal=macas*1.3
    print("O valor total das macas corresponde a : R$ {}".format(valorTotal))
else:
    valorTotal=macas
    print("O valor total das macas corresponde a : R$ {}".format(valorTotal))