# 9) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
# # Calcular e escrever o valor do novo salário.

salarioAtual=float(input("Digite o seu salario mensal atual: "))
percentualReajuste=float(input("Digite o percentual de reajuste: "))

# processamento
salarioFinal=salarioAtual*percentualReajuste/100+salarioAtual

print("O novo sálario com o reajuste ficou em: R$ {}".format(salarioFinal))