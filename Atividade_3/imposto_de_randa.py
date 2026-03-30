from os import system, name

def calcular_imposto(valor:float) -> float:
    valor_do_imposto = 0
    
    impostos = [(2259.21,2826.66,0.075), 
                (2826.66,3751.06,0.15), 
                (3751.06,4664.68,.225),
                (4664.68,float('inf'), 0.275)]

    for valor_inicial_da_taxa, valor_maximo_da_taxa, taxa in impostos: 

        if valor>valor_inicial_da_taxa:
            # Determina o teto do cálculo para a faixa atual:
            # Se o valor ultrapassa o limite da faixa, calcula sobre a faixa cheia.
            # Se o valor está dentro da faixa, calcula apenas sobre a parcela excedente.
            topo_do_calculo = min(valor,valor_maximo_da_taxa)

            valor_do_imposto += (topo_do_calculo - valor_inicial_da_taxa) * taxa
            
        else: #Se por acaso não estiver na faixa atual, então ele não estará nas próximas faixas, então pode parar
            break


    return valor_do_imposto


system('cls' if name == 'nt' else 'clear')

while(1):
    try: 
        valor = float(input("Digite o valor para que seja calculado o imposto: ").replace(",","."))
    # o ".replace(",",".")" vai substituir a vírgula por ponto, para que não dê erro na hora dá conversão
    #para float

        break #Vai ser calculado o imposto se somente o usuário digitar um valor válido
    except ValueError:
        print("O valor digital não foi aceito, digite novamente ")
        print()


resultado = calcular_imposto(valor)
print(f"Você terá que pagar {resultado:.2f}R$ de imposto ")   
