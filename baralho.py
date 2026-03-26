import random 
import os

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
        return f"{self.valor} de {self.naipe}"


class Baralho:

    def __init__(self):
        naipes = ["espadas", "ouros", "paus", "copas"]
        self.cartas = [Carta(v, n) for n in naipes for v in range(1, 14)]
        random.shuffle(self.cartas)

    def __len__(self):
        return len(self.cartas)
    
    def comprar_carta(self):
        return self.cartas.pop()

def vinte_e_um():

    baralho = Baralho()
    jogadores_ativos = int(input("Quantos jogadores vão jogar?"))
    jogadores = [Jogador(x) for x in range(jogadores_ativos)]

    for i in range(len(jogadores)):
        print("-------------------------\n")
        while True:
            print(f"Pontuação atual do {jogadores[i]}: {jogadores[i].pontuacao}")  
            resp = input("Desejas somar(S) ou passar(P)?\n").upper()
            
            match resp:
                case "S":
                    carta_comprada = baralho.comprar_carta()
                    print(f"Carta: {carta_comprada}\n")
                    print("-------------------------\n")
                    jogadores[i].pontuacao += carta_comprada.valor 

                    if jogadores[i].pontuacao == 21:
                        print(f"{jogadores[i]} ganhou o jogo!")
                        return
                    if jogadores[i].pontuacao > 21:
                        print("Você perdeu o jogo!\n")
                        break

                case "P":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
        
                case _:
                    print("Inválido")


    maior_pontuacao = max((j.pontuacao for j in jogadores if j.pontuacao <= 21), default= 0)
    vencedores = [str(j) for j in jogadores if j.pontuacao == maior_pontuacao]
    print("-------------------------\n")
    if maior_pontuacao == 0:
        print("Todo mundo perdeu.")
    else:
        print(f"Vencedor(es): {', '.join(vencedores)}")
        

vinte_e_um()


