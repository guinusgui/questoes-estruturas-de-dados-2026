import os
import random

def limpar_tela():
    #Código de limpeza do terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_regras():
    """Exibe as regras iniciais do jogo."""
    limpar_tela()
    texto = """
    ==================================================
              BEM-VINDO AO JOGO DE 21
    ==================================================
    
    OBJETIVO:
    Somar pontos com as cartas recebidas para chegar o 
    mais próximo possível de 21, sem ultrapassar!

    REGRAS:
    1. Cada jogador joga sua vez individualmente.
    2. Você pode pedir uma carta ('S') ou passar a vez ('P').
    3. Se você somar exatamente 21, você tem a melhor pontuação!
    4. Se passar de 21, você "estoura" e é eliminado.
    5. Se ninguém fizer 21, vence quem chegar mais perto.
    6. Valores das cartas: 1 a 13 pontos cada.

    ==================================================
    """
    print(texto)
    input("Pressione Enter para começar o jogo...")

class Jogador:
    def __init__(self, x):
        self.nome = x + 1
        self.pontuacao = 0

    def __str__(self):
        return f"Jogador {self.nome}"

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        # Retorna o valor direto, ex: "12 de Copas"
        return f"{self.valor} de {self.naipe}"

class Baralho:
    def __init__(self):
        naipes = ["Espadas", "Ouros", "Paus", "Copas"]
        # Cria um baralho completo com cartas de 1 a 13 para cada naipe
        self.cartas = [Carta(v, n) for n in naipes for v in range(1, 14)]
        random.shuffle(self.cartas) # Embaralha as cartas

    def __len__(self):
        return len(self.cartas)

    def comprar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop() # Tira a carta do topo
        return None

def vinte_e_um():
    mostrar_regras()
    limpar_tela()
    baralho = Baralho()

    
    while True:
        try:
            jogadores_ativos = int(input("Quantos jogadores vão jogar? "))
            if jogadores_ativos > 0: #Garanti o caso do usuário digitar um valor negativo
                break #Vai quebrar o loop quando o usuário mandar um inteiro maior que zero
            else:
                print("Por favor, digite um número maior que zero.\n")
        except ValueError: #Caso o usuário não digite um valor inteiro
            print("Resposta inválida! Digite apenas números inteiros.\n")

    jogadores = [Jogador(x) for x in range(jogadores_ativos)] #Aqui está sendo criado uma lista na qual para
    # cada indice da lista "jogadores" vai possuir um objeto "Jogador" 

    # Loop principal/Loop do jogo
    for i in range(len(jogadores)):
        limpar_tela()

        print(f"--- VEZ DO {str(jogadores[i]).upper()} ---")#Converte um objeto em uma string de texto, na qual
#essa função vai chamar o método "__str__", na qual esse foi configurado para retornar "Jogador {self.nome}"
        

        while True:

            print(f"\nSua pontuação atual: {jogadores[i].pontuacao}")  
            resp = input("Deseja pedir carta (S) ou passar (P)? ").strip().upper()
            #strip() vai retirar os espaçamentos no início e no final

            if resp == "S":
                carta_comprada = baralho.comprar_carta()
                
                if not carta_comprada:
                    print("As cartas do baralho acabaram!")
                    break #Acaba a vez do jogador quando acabar as cartas
                    
                print(f"-> Você comprou: {carta_comprada} (Vale {carta_comprada.valor} pontos)")
                jogadores[i].pontuacao += carta_comprada.valor 

                if jogadores[i].pontuacao == 21:
                    print(f"\nParabéns! Você alcançou os 21 PONTOS! Seu turno acabou.")
                    input("Pressione Enter para passar a vez...")
                    break #Acaba a vez do jogador quando ele alcançar os 21 pontos
                
                elif jogadores[i].pontuacao > 21:
                    print(f"\nESTOUROU! Pontuação final: {jogadores[i].pontuacao}. Você foi eliminado!")
                    input("Pressione Enter para passar a vez...")
                    break #Acaba a vez do jogador quando ele ultrapassar os 21 pontos
                    
            elif resp == "P":
                print(f"Você decidiu parar com {jogadores[i].pontuacao} pontos.")
                input("Pressione Enter para passar a vez...")
                break
                
            else:
                print("Opção inválida! Digite 'S' para pedir ou 'P' para passar.")

    # Resultado Final
    limpar_tela()

    texto = """
==================================================
            RESULTADO FINAL
================================================== """
    
    print(texto)
    
    # Exibe a pontuação final de todos os jogadores
    for j in jogadores:
        status = " (ESTOUROU)" if j.pontuacao > 21 else ""
        print(f"{j}: {j.pontuacao} pontos{status}")

    # Encontrar os ganhadores (ignora quem passou de 21)
    maior_pontuacao = max((j.pontuacao for j in jogadores if j.pontuacao <= 21), default=0)
    vencedores = [str(j) for j in jogadores if j.pontuacao == maior_pontuacao]
    
    print("\n--------------------------------------------------")
    if maior_pontuacao == 0:
        print("TODO MUNDO PERDEU! Todos ultrapassaram 21 pontos.")
    else:
        print(f"🏆 VENCEDOR(ES) COM {maior_pontuacao} PONTOS: {', '.join(vencedores)} 🏆")
    print("--------------------------------------------------\n")

# Inicia o jogo
if __name__ == "__main__":
    vinte_e_um()
