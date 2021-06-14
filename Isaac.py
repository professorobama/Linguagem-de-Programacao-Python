#30) Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem
#crescente.

valor1 = int (input("Digite o primeiro valor: "))
valor2 = int (input("Digite o segundo valor: "))
valor3 = int (input("Digite o terceiro valor: "))

if valor1>valor2 and valor2>valor3:
    print("ORDEM CRESCENTE: {},".format(valor3),"{},".format(valor2),"{}!".format(valor1))
elif valor2>valor1 and valor1>valor3:
    print("ORDEM CRESCENTE: {},".format(valor3),"{},".format(valor1),"{}!".format(valor2))
elif valor3>valor2 and valor2>valor1:
    print("ORDEM CRESCENTE: {},".format(valor1),"{},".format(valor2),"{}!".format(valor3))
elif valor1>valor3 and valor3>valor2:
    print("ORDEM CRESCENTE: {},".format(valor2),"{},".format(valor3),"{}!".format(valor1))
elif valor2>valor3 and valor3>valor1:
    print("ORDEM CRESCENTE: {},".format(valor1),"{},".format(valor3),"{}!".format(valor2))
else:
    print("ORDEM CRESCENTE: {},".format(valor2),"{},".format(valor1),"{}!".format(valor3))
