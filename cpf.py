import re

def obter_digitos():
    """Função responsável por obter cpfs com formatação correta(11 caracteres e somente números)"""
    cpf = []
    while True: 
        cpf = input("Digite o seu CPF(11 dígitos): ")
        cpf = list(re.sub('\D', '', cpf)) #remove espaços e outros digitos e outros caracteres indesejados como '.', '-' e retorna uma lista de caracteres e 
        if len(cpf) == 11:
            cpf = [int(i) for i in cpf] #converte cada item da lista para inteiro
            return cpf
        else:
            print("Um CPF deve conter 11 números. Tente novamente.")
        

def obter_resto(cpf, n):
    """Calcula a soma dos produtos dos números repassados e retorna o resto da sua divisão por 11"""
    soma = 0                                                
    for i in range(n):
        soma += cpf[i]*((n+1)-i)
    return soma%11

def validacao(cpf):
    """Recebe o cpf e o verifica com base nos casos testes."""

    if cpf == [cpf[0]]*11: #trata casos de cpfs com números repetidos(ex: 000.000.000-00) que passam pelos
        return False        #cálculos verificadores, mas não são válidos.
    
    resto = obter_resto(cpf, 9)
    digito_esperado = 0 if resto < 2 else 11 - resto 
    
    if digito_esperado != cpf[9]:
        return False
    
    resto2 = obter_resto(cpf, 10)
    digito_esperado = 0 if resto2 < 2 else 11 - resto2

    if digito_esperado != cpf[10]: 
        return False
    
    return True     #Se nenhuma das condições falseadoras se cumprir, retorna True.

cpf = obter_digitos()

if validacao(cpf):     #Imprime o resultado com base no retornado pela função validação(True ou False)
    print("CPF válido!")
else:
    print("CPF inválido!")


    
