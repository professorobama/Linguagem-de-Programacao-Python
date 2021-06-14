
nome=str(input("Digite o seu nome:"))
altura= float(input("Digite a sua altura:"))
sexo=str(input("Digite o seu sexo:"))

if sexo =="M" or "m" or "Masc" or "masc" or "Masculino" or "masculino":
    pesoIdeal=72.7*altura-58
else:
    pesoIdeal=62.1*altura-44.7    
print("Para o sexo {}".format(sexo), "o peso ideal é : {}".format(pesoIdeal))