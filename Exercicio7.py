#7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
#dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

anos=int(input("Digite a sua idade expressa em anos:"))
meses=int(input("Digite a quantidade de meses que passou do seu aniversário:"))
dias=int(input("Digite a quantidade de dias que passou do seu ultimo mesaniversário:"))
totalVivido=(anos*365)+(meses*30)+dias
print("A quantidade de dias vividos pela pessoa corresponde a : {}".format(totalVivido))