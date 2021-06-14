#29) Ler 3 valores (considere que não serão informados valores iguais) 
# e escrever a soma dos 2 maiores.

numero1=int(input("Digite o 1º numero :"))
numero2=int(input("Digite o 2º numero :"))
numero3=int(input("Digite o 3º numero :"))

if  numero1<numero2 and numero2<numero3:
    soma=numero2+numero3
    print("A soma do maiores valores é : {}".format(soma))
elif  numero1<numero2 and numero2>numero3 and numero1<numero3:
    soma=numero2+numero3
    print("A soma do maiores valores é : {}".format(soma))
elif  numero1>numero2 and numero2<numero3:
    soma=numero1+numero3
    print("A soma do maiores valores é : {}".format(soma))
elif  numero1<numero2 and numero2>numero3:
    soma=numero1+numero2
    print("A soma do maiores valores é : {}".format(soma))
elif  numero1>numero2 and numero2<numero3:
    soma=numero1+numero3
    print("A soma do maiores valores é : {}".format(soma))
else:
    soma=numero1+numero2
    print("A soma do maiores valores é : {}".format(soma))
    
#Teste de Mesa    
#123*//
#1<3>2  1<2*********//
#213*//
#2<3>1*********//
#312*//
#321*