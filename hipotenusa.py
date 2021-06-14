# Calculo da Hipotenusa em Python
#a²=b²+c²
import math

cateto1=float(input("Digite o primeiro valor do cateto :"))
cateto2=float(input("Digite o segundo valor do cateto :"))
hipotenusa=(cateto1*cateto1)+(cateto2*cateto2)
hipotenusa2=math.sqrt(hipotenusa)

print("O calculo do cateto {} mais o cateto {} resulta na hipotenusa : {}".format(cateto1,cateto2,hipotenusa2))
