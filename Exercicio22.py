# 22) A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais
# de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%.
# Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva
# o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas
# (considere que o mês possua 4 semanas exatas).

horasTrabalhadasMes=int(input("Digite a quantidade de horas trabalhas no mês:"))
salarioHora= float(input("Digite o seu salario recebido por hora:"))

if horasTrabalhadasMes<=160:
    salarioFinal=horasTrabalhadasMes*salarioHora
    print("O salário final do funcionário corresponde a: R$ {}".format(salarioFinal))
else:
    salarioFinal=(horasTrabalhadasMes*salarioHora) + (horasTrabalhadasMes-160)*50/100*salarioHora
    print("O salário final do funcionário corresponde a: R$ {}".format(salarioFinal))