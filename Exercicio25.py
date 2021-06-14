# 25) Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e
# escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior
# ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

numeroContaCliente=int(input("Digite o numero da sua conta:"))
saldo=float(input("Digite o saldo da sua conta:"))
debito=float(input("Digite a quantidade de debito da sua conta:"))
credito=float(input("Digite a quantidade de créditoda sua conta:"))

saldoAtual= saldo-debito+credito

if saldoAtual>=0:
    print("Saldo Positivo {}".format(saldoAtual))
else:
    print("Saldo Negativo{}".format(saldoAtual))