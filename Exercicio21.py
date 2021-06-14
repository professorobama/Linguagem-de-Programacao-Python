# 21) Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os
# minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é
# de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

horaInicio = int (input("Digite o hora de início do jogo de Xadrez:"))
horaFim = int (input("Digite o hora de fim do jogo de Xadrez:"))
duracao = horaFim - horaInicio
if duracao<0:
    duracao= duracao +24
    print("A duração do jogo de Xadrez corresponde a : {}".format(duracao), " horas")
else:
    print("A duração do jogo de Xadrez corresponde a : {}".format(duracao), " horas")