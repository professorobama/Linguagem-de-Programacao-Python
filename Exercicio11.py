# Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
# mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
# efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
# vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
# vendedor.

# Variáveis de entrada

numeroCarroVendidos=int(input("Digite a quantidade de carros vendidos pelo funcionário: "))
valorTotalVendas=float(input("Digite o valor total de vendas: "))
salarioFixo=float(input("Digite o valor do salário fixo: "))
comissao=float(input("Digite o valor da comissão: "))

salarioFinal=salarioFixo+ (comissao*numeroCarroVendidos) + (5/100*valorTotalVendas)

print("O salário final do vendedor é de : R$ {}".format(salarioFinal))