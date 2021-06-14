# 24) Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que
# ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que
# ultrapassar este valor, calcular e escrever o seu salário total.

salarioFixo=float(input("Digite o seu salário fixo:"))
valorVendas=float(input("Digite o valor total das vendas:"))

if valorVendas<=1500:
    salarioFinal=salarioFixo + valorVendas*3/100
    print("O valor do salario final do funcionário corresponde a : R$ {}".format(salarioFinal))
else:
    salarioFinal=salarioFixo + (valorVendas-1500)*5/100 + (1500*3/100)
    print("O valor do salario final do funcionário corresponde a : R$ {}".format(salarioFinal))