#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e
#quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade
#média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual
#a quantidade média escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar
#compra'.

quantidadeatual=int(input("Digite a quantidade atual do produto em estoque: "))
quantidademaxima=int(input("Digite a quantidade máxima do produto em estoque: "))
quantidademinima=int(input("Digite a quantidade mínima do produto em estoque: "))

quantidademedia=(quantidademaxima+quantidademinima)/2

if quantidadeatual>=quantidademedia:
    print('Não efetuar compra')
else:
    print('Efetuar compra')    