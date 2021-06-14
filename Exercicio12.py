# 12) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor
# correspondente em graus Celsius (baseado na fórmula abaixo):
# C/5= F-32/9
# Observação: Para testar se a sua resposta está correta saiba que 100°C = 212°F

Fahrenheit=float(input("Digite a temperatura em graus Fahrenheit :"))
grausCelsius= (Fahrenheit-32)/9*5
print("A tempratura em graus Celsius é: {} °C".format(grausCelsius))
