#31) Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo
#e escrever se formam ou não um triângulo. OBS: para formar um triângulo,
#o valor de cada lado deve ser menor que a soma dos outros 2 lados.


lado1=int(input("Digite o 1º lado :"))
lado2=int(input("Digite o 2º lado :"))
lado3=int(input("Digite o 3º lado :"))

if  lado1<lado2+lado3 and  lado2<lado1+lado3 and lado3<lado1+lado2:
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")
    
    #123 F
    #132 F
    #213 F
    #231 F
    #312 F
    #321 F