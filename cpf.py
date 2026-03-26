import re

def obter_digitos():
    cpf = []
    while(len(cpf) != 11):
        cpf = input("Digite o seu CPF[11 dígitos]: ")
        cpf = list(re.sub('\D', '', cpf)) 
    cpf = [int(i) for i in cpf]
    return cpf

def obter_resto(cpf, n):
    soma = 0                                                
    for i in range(n):
        soma += cpf[i]*((n+1)-i)
    return soma%11

def validacao(cpf):

    if cpf == [cpf[0]]*11:
        return False
    
    resto = obter_resto(cpf, 9)

    if (resto < 2 and cpf[9] != 0) or (cpf[9] != (11 - resto)):
        return False
    
    resto2 = obter_resto(cpf, 10)

    if (resto2 < 2 and cpf[10] != 0) or (cpf[10] != (11 - resto2)):
        return False
    
    return True

cpf = obter_digitos()

if validacao(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")


    
