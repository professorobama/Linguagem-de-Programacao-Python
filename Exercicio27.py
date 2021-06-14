#27) Ler um valor e escrever se é positivo, negativo ou zero.

numero= int(input("Digite um número:"))

if numero<0:
    print("O número digitado é negativo")
elif numero == 0:
    print("O número digitado é Zero")
else:
    print("O número digitado é positivo")
