# 18) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela
# poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

anoAtual = int (input("Digite o ano atual:"))
anoNascimento = int (input("Digite o seu ano de nascimento:"))

idade=anoAtual-anoNascimento
if idade<16:
    print("A idade da pessoa corresponde a :{}".format(idade), "e você não pode votar")
else:
    print("A idade da pessoa corresponde a :{}".format(idade), "e você pode votar")