# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
# brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
# de eleitores.

# Criação das variáveis
numeroTotalEleitores=int(input("Digite o número total de eleitores:"))
numeroTotalVotosBrancos=int(input("Digite o número total de votos brancos:"))
numeroTotalVotosNulos=int(input("Digite o número total de votos nulos:"))
numeroTotalVotosValidos=int(input("Digite o número total de votos válidos:"))
# Processamento
porcetagemVotosBrancos=numeroTotalVotosBrancos/numeroTotalEleitores*100
porcetagemVotosNulos=numeroTotalVotosNulos/numeroTotalEleitores*100
porcetagemVotosValidos=numeroTotalVotosValidos/numeroTotalEleitores*100
# Saída
print("A porcentagem de votos brancos corresponde a : {} %".format(porcetagemVotosBrancos))
print("A porcentagem de votos nulos corresponde a : {} %".format(porcetagemVotosNulos))
print("A porcentagem de votos válidos corresponde a : {} %".format(porcetagemVotosValidos))
