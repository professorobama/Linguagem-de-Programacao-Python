#28) Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

numero1=int(input("Digite o 1º numero :"))
numero2=int(input("Digite o 2º numero :"))
numero3=int(input("Digite o 3º numero :"))

if numero1>numero2 and numero1>numero3:
    print("O maior numero digitado é :{}".format(numero1))
elif numero2>numero1 and numero2>numero3:
    print("O maior numero digitado é :{}".format(numero2))
elif numero1==numero2 or numero1==numero3 or numero2== numero3:
    print("Numero iguais")     
else:    
    print("O maior numero digitado é :{}".format(numero3))
